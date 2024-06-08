from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.body[:20]}"

class Question(models.Model):
    branche = models.CharField(max_length=100)
    thème = models.CharField(max_length=200)
    prénom = models.CharField(max_length=100)
    question_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text

class Reponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    prénom = models.CharField(max_length=100)
    réponse_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.réponse_text