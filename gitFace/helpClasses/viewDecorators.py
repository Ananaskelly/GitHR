from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import github
from github import BadCredentialsException, RateLimitExceededException


def valid_token_required(function=None):
    """
    Verify that request object contains token.
    Otherwise it will be redirected on homepage
    """

    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if 'token' in request.session:
                try:
                    git = github.Github(request.session['token'])
                    if git.get_api_status().status == 'good':
                        kwargs['gitConn'] = git
                        return view_func(request, *args, **kwargs)
                except (BadCredentialsException, RateLimitExceededException) as e:
                    pass
            return redirect('/')

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)