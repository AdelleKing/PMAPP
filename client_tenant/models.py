from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True, default=timezone.now)
    status  = models.IntegerField(null=True)
    description = models.TextField(null=True)
       

    def __str__(self):
        return self.name


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        try:
            return f'{self.text[:20]}'
        except:
            return f'no comments'
    

