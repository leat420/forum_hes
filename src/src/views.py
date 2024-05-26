# src/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def opinions(request):
    return render(request, 'opinions.html')

def question_reponses(request):
    return render(request, 'question_reponses.html')
