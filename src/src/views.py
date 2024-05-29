# src/views.py
from django.shortcuts import render, redirect
from django import forms
from .forms import CommentForm
from .models import Comment



def index(request):
    return render(request, 'index.html')


def opinions(request):
    return render(request, 'opinions.html')


def question_reponses(request):
    return render(request, 'question_reponses.html')


def comment_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('FORUM.html')
            #redirige vers une page de confirmation ou une autre vue
    else:
        form = CommentForm()
    return render(request, 'question_reponses.html', {'form': form})

def show_comments(request):
    comments = Comment.objects.all()
    return