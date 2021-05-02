from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Post(models.Model):

    user = models.ForeignKey(User, related_name='posts', on_delete=models.SET_NULL, null=True)
    caption = models.CharField(max_length=255, blank=True)
    recipe = models.TextField(blank=False)
    image = models.ImageField(upload_to='post_pics', null=True)
    likes = models.ManyToManyField(User, related_name='post_user', blank=True, through=PostLike)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['-id']

