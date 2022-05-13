from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=256, help_text="Enter your post title")
    image = models.ImageField(upload_to='blog-images/')
