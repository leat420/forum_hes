from django.shortcuts import render, redirect
from .forms import CommentForm, QuestionForm, AnswerForm
from .models import Comment, Question, Answer
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'index.html')


def opinions(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.created_at = timezone.now()
            new_comment.save()
            return redirect('opinions')
    else:
        form = CommentForm()

    comments = Comment.objects.all()
    context = {
        'comments': comments,
        'form': form
    }
    return render(request, 'opinions.html', context)


def display_comments(request):
    # Fetch all comments from the database
    comments = Comment.objects.all()

    # Render the HTML template and pass in the comments
    context = {'comments': comments}
    return render(request, 'your_template.html', context)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        comment.delete()
        return redirect('opinions')
    return render(request, 'delete_comment.html', {'comment': comment})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.created_at = timezone.now()
            new_comment.save()
            return redirect('create_question')  # Redirection après la soumission réussie
    else:
        form = QuestionForm()

    questions = Question.objects.all().order_by('-created_at')  # Récupère toutes les questions pour les afficher

    return render(request, 'create_question.html', {'form': form, 'questions': questions})


def question_detail(request):
    questions = Question.objects.all()

    context = {'questions': questions}
    return render(request, 'your_template.html', context)


def delete_question(request, question_id):
    if request.method == "POST":
        question = get_object_or_404(Question, id=question_id)
        question.delete()
        return redirect('create_question')
    else:
        return redirect('create_question')
