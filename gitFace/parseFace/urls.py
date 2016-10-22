
from django.conf.urls import url, include
from rest_framework import routers
from . import views

urlpatterns = [
    # Additionally, we include login URLs for the browsable API.
    # слово + дефис + любое их количество до слеша /
    url(r'^$', views.main_page, name='main'),
    url(r'^callback/', views.callback, name='callback'),
    url(r'^(?P<profile_name>[\w\-]+)/$', views.hello, name='hello'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
