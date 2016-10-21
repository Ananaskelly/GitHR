
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from gitFace.helpClasses.JSONResponse import JSONResponse
from rest_framework.parsers import JSONParser
from .entities import *
from .serializer import *


# serializer = SnippetSerializer(snippets, many=True)
# serializer.data -- just JSON representation


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
