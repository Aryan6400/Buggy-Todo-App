from django.db import models


class Todo(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(blank=False, null=False)
    updated_at = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.title
