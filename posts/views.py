from django.shortcuts import render
from django.http import request
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from . models import Post
from . serializers import PostSerializer

# Create your views here.

class ListPostAPIView(ListAPIView):
    """This endpoint lists all posts"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreatePostAPIView(CreateAPIView):
    """This endpoint allows for creation of a post"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdatePostAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific post"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeletePostAPIView(DestroyAPIView):
    """This endpoint allows for deleting a specific post"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RetrievePostAPIView(RetrieveAPIView):
    """This endpoint allows for retrieving a specific post"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer