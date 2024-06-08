from django.shortcuts import render, redirect
from .forms import CommentForm, QuestionForm
from .models import Comment, Question
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment  # Assuming you have a Comment model


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
    questions = Question.objects.all()  # Récupérer toutes les questions
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_question')
    else:
        form = QuestionForm()
    context = {
        'form': form,
        'questions': questions  # Ajouter les questions au contexte
    }
    return render(request, 'create_question.html', context)
class AnswerForm:
    pass


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('question_detail', question_id=question_id)
    else:
        form = AnswerForm()
    answers = question.answers.all()
    return render(request, 'question_detail.html', {'question': question, 'answers': answers, 'form': form})