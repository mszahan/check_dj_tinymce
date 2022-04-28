from django.db import models
from tinymce.models import HTMLField 


class Post(models.Model):
    title = models.CharField(max_length=250)
    content =  HTMLField()

    def __str__(self):
        return self.title
    

class Figure(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='figures')
    title = models.CharField(max_length=250)
    # caption = models.TextField()
    image = models.ImageField(upload_to='figures/%Y/%M')

