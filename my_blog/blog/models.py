from turtle import title
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image  = models.FileField(upload_to="article_imgs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title