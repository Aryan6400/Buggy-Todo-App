from django.db import models
from .serializers import TodoSerializer


class Todo(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.author = ''
        super(Todo, self).save(*args, **kwargs)
    
    @property
    def data(self):
        return TodoSerializer(self).data
