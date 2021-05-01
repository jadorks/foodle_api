from django.urls import path
from . import views

urlpatterns = [

    path("", views.ListPostAPIView.as_view(), name="post_list"),
    path("create", views.CreatePostAPIView.as_view(), name="post_create"),
    path("view/<int:pk>", views.RetrievePostAPIView.as_view(), name="post_view"),
    path("delete/<int:pk>", views.DeletePostAPIView.as_view(), name="post_delete"),

]