from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from gitFace.helpClasses.JSONResponse import JSONResponse
from rest_framework.parsers import JSONParser
from .entities import *
from .serializer import *

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

import github

# serializer = SnippetSerializer(snippets, many=True)
# serializer.data -- just JSON representation


def main_page(request):
    return render(request, 'home.html', {"clientId" : "e367ac8d3b8fea3451b4"})


def callback(request):

    if request.method == 'GET':
        temp_code = request.GET.get('code', 'absent')

        url = 'https://github.com/login/oauth/access_token'  # Set destination URL here
        post_fields = {'client_id': 'e367ac8d3b8fea3451b4',
                       'client_secret': '451bd4a6a6127b76acb947696e0a43e448fe7d83',
                       'code': temp_code}  # Set POST fields here
        headers = {'Accept': 'application/json'}
        request = Request(url, urlencode(post_fields).encode(), headers)
        json_data = urlopen(request).read().decode()

        token = json.loads(json_data).get('access_token', None)

        gitConn = github.Github(token)



        response = HttpResponse(gitConn.get_user().name + "<br>" +
                                str(gitConn.get_rate_limit().rate.remaining) + "<br>" +
                                gitConn.get_api_status().status + "<br>" +
                                str(gitConn.get_user("learp").public_repos))
        # response.set_cookie()



        return response

    return Http404("wrong callback")


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
