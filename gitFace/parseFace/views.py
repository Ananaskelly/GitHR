import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from gitFace.gitFaceConf import AppGitHubKeys, MainPageString
from gitFace.helpClasses.JSONResponse import JSONResponse
from gitFace.helpClasses.api_services import get_profile_dict
from gitFace.helpClasses.viewDecorators import valid_token_required, api_exception_catcher


def test_page(request):
    return render(request, 'home.html', {"clientId": "e367ac8d3b8fea3451b4"})


def main_page(request):
    response = HttpResponse(MainPageString)
    return response


def have_token(request):
    return HttpResponse(str('token' in request.session))


@require_http_methods(["GET"])
@valid_token_required
@api_exception_catcher
def get_repos(request, profile_name, gitConn = None):
    user = gitConn.get_user(profile_name)
    l1 = [rep for rep in user.get_repos("all")]
    l2 = [rep for rep in user.get_subscriptions()]
    # l3 = [rep for rep in user.get_watched()] #Есть некоторые просто со звёздами, в них кусочки кода
    repos = l1 + l2

    full_data = {}
    for rep in repos:
        if rep.full_name not in full_data:
            full_data[rep.full_name] = {
                'full_name': rep.full_name,
                'name': rep.name,
                'description': rep.description,
                'html_url': rep.html_url,
                'homepage': rep.homepage,
                'stars': rep.watchers,
                'forks': rep.forks,
                'size': rep.size,
                'language': rep.language,
                'created_at': rep.created_at.strftime("%d-%m-%Y"),
                'updated_at': rep.updated_at.strftime("%d-%m-%Y"),
            }

    return JSONResponse(full_data)


@require_http_methods(["GET"])
@valid_token_required
@api_exception_catcher
def token_profile(request, gitConn = None):
    return JSONResponse(get_profile_dict(git_conn=gitConn))


@require_http_methods(["GET"])
@valid_token_required
@api_exception_catcher
def get_profile(request, profile_name, gitConn = None):
    return JSONResponse(get_profile_dict(git_conn=gitConn, profile_name=profile_name))


@require_http_methods(["GET"])
@valid_token_required
@api_exception_catcher
def present(request, gitConn = None):
    context = {
        'login': gitConn.get_user().login,
        'limit': str(gitConn.get_rate_limit().rate.remaining),
        'repos': str(gitConn.get_user().public_repos),
        'repos_name': str([i.name for i in gitConn.get_user().get_repos()]),
        'followers': str(gitConn.get_user().followers),
               }

    return render(request, "presentation.html", context)


@require_http_methods(["GET"])
def callback(request):
    error = ""
    if 'code' in request.GET:

        temp_code = request.GET['code']
        url = 'https://github.com/login/oauth/access_token'
        # Set POST fields here
        post_fields = {
            'client_id': AppGitHubKeys.client_id,
            'client_secret': AppGitHubKeys.client_secret,
            'code': temp_code
                       }
        headers = {'Accept': 'application/json'}
        request_git = Request(url, urlencode(post_fields).encode(), headers)

        json_data = urlopen(request_git).read().decode()
        data = json.loads(json_data)

        if 'error' not in data:
            request.session['token'] = data['access_token']
            # return HttpResponse("Your new token : " + data['access_token'])
            return redirect('/')
        else:
            error += data['error']
    else:
        error += "absent code"

    return HttpResponse("wrong callback: " + error)


