import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from gitFace.gitFaceConf import AppGitHubKeys, MainPageString
from gitFace.helpClasses.JSONResponse import JSONResponse
from gitFace.helpClasses.api_services import get_profile_dict
from gitFace.helpClasses.viewDecorators import valid_token_required, api_exception_catcher


def test_page(request):
    return render(request, 'home.html', {"clientId": "e367ac8d3b8fea3451b4"})


def main_page(request):
    return HttpResponse(MainPageString)


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
            return HttpResponse("Your new token : " + data['access_token'])
        else:
            error += data['error']
    else:
        error += "absent code"

    return HttpResponse("wrong callback: " + error)


