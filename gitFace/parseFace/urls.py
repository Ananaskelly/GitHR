
from django.conf.urls import url, include
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main'),
    url(r'^test/$', views.test_page, name='main'),
    url(r'^callback/', views.callback, name='callback'),
    url(r'^present/', views.present, name='present'),
    url(r'^current/', views.token_profile, name='token_profile'),
    # Additionally, we include login URLs for the browsable API.
    # слово + дефис + любое их количество до слеша /
    url(r'^api/(?P<profile_name>[\w\-]+)/$', views.get_profile, name='get_profile'),
]
