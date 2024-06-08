from .models import Comment, Question, Answer
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['branche', 'theme', 'name', 'question_text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['name', 'answer_text']
