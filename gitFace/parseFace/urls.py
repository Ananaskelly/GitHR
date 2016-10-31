
from django.conf.urls import url, include
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^test/$', views.test_page, name='main'),
    url(r'^callback/', views.callback, name='callback'),
    url(r'^present/', views.present, name='present'),
    url(r'^current/', views.token_profile, name='token_profile'),
    url(r'^token/', views.have_token, name='token_presence'),
    # Additionally, we include login URLs for the browsable API.
    # слово + дефис + любое их количество до слеша /
    url(r'^api/(?P<profile_name>[\w\-]+)/$', views.get_profile, name='get_profile'),
    url(r'^api/repos/(?P<profile_name>[\w\-]+)/$', views.get_repos, name='get_repos'),
    url(r'^$', views.main_page, name='main'),
]


