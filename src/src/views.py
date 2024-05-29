from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

def index(request):
    return render(request, 'index.html')

def opinions(request):
    return render(request, 'opinions.html')

def question_reponses(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_reponses')
    else:
        form = CommentForm()

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'question_reponses.html', {'form': form, 'comments': comments})
