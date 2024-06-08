from django import forms
from .models import Comment, Question, Reponse
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['branche', 'thème', 'prénom', 'question_text']

class Reponse(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ['prénom', 'réponse_text']
