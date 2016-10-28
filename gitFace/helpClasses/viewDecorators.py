import time
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
import github
from github import BadCredentialsException, RateLimitExceededException
from github import UnknownObjectException


# catch all common parse exception and return response by convention
def api_exception_catcher(the_func):
    def _decorated(*args, **kwargs):
        try:
            res = the_func(*args, **kwargs)
            return res
        except RateLimitExceededException as e:
            return HttpResponseForbidden('token_limit')
        except BadCredentialsException as e:
            return HttpResponseForbidden('badkey')
        except UnknownObjectException as e:
            return HttpResponseNotFound('not_found')

    _decorated.__name__ = the_func.__name__
    _decorated.__dict__ = the_func.__dict__
    _decorated.__doc__ = the_func.__doc__

    return _decorated


def valid_token_required(function=None):
    """
    Verify that request object contains token.
    Otherwise it will be redirected on homepage
    to get this token
    """

    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if 'token' in request.session:
                try:
                    git = github.Github(request.session['token'])
                    if git.get_api_status().status == 'good':
                        kwargs['gitConn'] = git
                        return view_func(request, *args, **kwargs)
                except RateLimitExceededException as e:
                    return HttpResponseForbidden('token_limit')
                except BadCredentialsException as e:
                    return HttpResponseForbidden('badkey')
            return HttpResponseForbidden('require_token')

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)