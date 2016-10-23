from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from github import RateLimitExceededException
from github import UnknownObjectException
from rest_framework import viewsets

from gitFace.gitFaceConf import AppGitHubKeys

from gitFace.helpClasses.JSONResponse import JSONResponse
from rest_framework.parsers import JSONParser
from .entities import *
from .serializer import *

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

import github

from gitFace.helpClasses.viewDecorators import valid_token_required
# serializer = SnippetSerializer(snippets, many=True)
# serializer.data -- just JSON representation


def main_page(request):
    return render(request, 'home.html', {"clientId" : "e367ac8d3b8fea3451b4"})

@valid_token_required
def token_profile(request, gitConn = None):

    if request.method == 'GET':
        user = gitConn.get_user()
        response = user.raw_data
        response['repos_count'] = len(list(user.get_repos()))
        return JSONResponse(json.dumps(response))

    return Http404("bad method")

@valid_token_required
def get_profile(request, profile_name, gitConn = None):

    if request.method == 'GET':
        try:
            user = gitConn.get_user(profile_name)
            repos = list(user.get_repos())

            response = user.raw_data
            response['repos_count'] = len(repos)
            response['repos_names'] = [rep.name for rep in repos]

        except UnknownObjectException as e:
            return HttpResponse("this profile doesn't exist")
        except RateLimitExceededException as e:
            return HttpResponse("your have consumed all your limit")

        return JSONResponse(json.dumps(response))

    return Http404("bad method")

@valid_token_required
def present(request, gitConn = None):
    context = {
        'login': gitConn.get_user().login,
        'limit': str(gitConn.get_rate_limit().rate.remaining),
        'repos': str(gitConn.get_user().public_repos),
        'repos_name': str([i.name for i in gitConn.get_user().get_repos()]),
        'followers': str(gitConn.get_user().followers),
               }
    return render(request, "presentation.html", context)


def callback(request):
    error = ""
    if request.method == 'GET' and 'code' in request.GET:

        temp_code = request.GET['code']
        url = 'https://github.com/login/oauth/access_token'
        # Set POST fields here
        post_fields = {
            'client_id': AppGitHubKeys['client_id'],
            'client_secret': AppGitHubKeys['client_secret'],
            'code': temp_code
                       }
        headers = {'Accept': 'application/json'}
        request_git = Request(url, urlencode(post_fields).encode(), headers)

        json_data = urlopen(request_git).read().decode()
        data = json.loads(json_data)

        if 'error' not in data:
            request.session['token'] = data['access_token']
            return HttpResponse("Your new token : " + data['access_token'])
        else:
            error += data['error']
    else:
        error += "bad method or absent code"

    return HttpResponse("wrong callback: " + error)


@csrf_exempt
def hello(request, profile_name):

    comments = [Comment("luga2012@yandex.ru", "Hi, how are you today?")] * 2
    serializer = CommentSerializer(comments, many=True)
    if request.method == 'GET':
        return JSONResponse(serializer.data)
        # return JSONResponse(serializer.data, status=201)

        # I wait BODY with JSON
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        print("parsed")
        serializer = CommentSerializer(data=data, many=True)
        if serializer.is_valid():
            # attempt to change object
            serializer.save()[0].email = "today@today.com"
            return JSONResponse(serializer.data, status=201)

    return JSONResponse(serializer.errors, status=400)
