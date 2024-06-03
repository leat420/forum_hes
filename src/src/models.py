from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.body[:20]}"


class HelpRequest(models.Model):
    Branche = models.CharField(max_length=20)
    Thème = models.CharField(max_length=200)
    Prénom = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    Question = models.TextField()

    def __str__(self):
        return self.Thème


class Response(models.Model):
    help_request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE, related_name='responses')
    responder_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    answer = models.TextField()

    def __str__(self):
        return f"Response to {self.help_request.Thème} by {self.responder_name}"
