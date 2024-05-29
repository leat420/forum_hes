from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name
