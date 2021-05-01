from django.db import models

# Create your models here.
class Post(models.Model):
    caption = models.CharField(max_length=255, blank=True)
    recipe = models.TextField(blank=False)
    image = models.ImageField(upload_to='posts/', null=True)

    def __str__(self):
        return self.caption