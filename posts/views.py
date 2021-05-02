from django.shortcuts import render, get_object_or_404
from django.http import request
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import filters
from . models import Post
from django.contrib.auth.models import User
from . serializers import PostSerializer, UserSerializer, PostActionSerializer

# Create your views here.

class ListPostAPIView(ListAPIView):
    """This endpoint lists all posts"""

    search_fields = ['recipe']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreatePostAPIView(CreateAPIView):
    """This endpoint allows for creation of a post"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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

class ListUserAPIView(ListAPIView):
    """This enpoint lists all the users"""

    search_fields = ['^username']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUserAPIView(ListAPIView):
    """This endpoint retrieves the current logged in user"""

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id = self.request.user.id)


class RetrieveUserAPIView(RetrieveAPIView):
    """This endpoint shows the details for a specific user"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUserPostAPIView(ListAPIView):
    """This endpoint lists the posts of the logged in user"""
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(user = self.request.user.id)

class UserPostAPIView(ListAPIView):
    """This endpoint lists the posts of a specific user"""
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk', None)
        if user_id is not None:
            user = get_object_or_404(User, id=user_id)
            return Post.objects.filter(
                user = user
            ).all()
        else:
            return Post.objects.none()


@api_view(['POST'])
def post_action_view(request, *args, **kwargs):


    serializer = PostActionSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        post_id = data.get("id")
        action = data.get("action")
       
        qs = Post.objects.filter(id=post_id)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()

        if action == "like":
            obj.likes.add(request.user)
            return Response({"msg": "liked"}, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            return Response({"msg": "unliked"}, status=200)

    return Response({"msg": "Post Liked"}, status=200)