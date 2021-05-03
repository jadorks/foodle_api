from django.urls import path
from . import views

urlpatterns = [

    path("", views.ListPostAPIView.as_view(), name="post_list"),
    path("create/", views.CreatePostAPIView.as_view(), name="post_create"),
    path("update/<int:pk>/", views.UpdatePostAPIView.as_view(), name="post_update"),
    path("view/<int:pk>/", views.RetrievePostAPIView.as_view(), name="post_view"),
    path("delete/<int:pk>/", views.DeletePostAPIView.as_view(), name="post_delete"),

    path("users/", views.ListUserAPIView.as_view(), name="users_list"),
    path("user/", views.CurrentUserAPIView.as_view(), name="current_user"),
    path("users/posts/<int:pk>/", views.UserPostAPIView.as_view(), name="users_posts"),
    path("users/posts/", views.CurrentUserPostAPIView.as_view(), name="current_posts"),
    path("users/<int:pk>/", views.RetrieveUserAPIView.as_view(), name="user_details"),

    path("action/", views.post_action_view)

]