from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import HelpRequestForm, ResponseForm
from .models import HelpRequest

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


def help_requests(request):
    requests = HelpRequest.objects.all().order_by('-created_at')
    return render(request, 'help_requests.html', {'requests': requests})

def new_help_request(request):
    if request.method == 'POST':
        form = HelpRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('help_requests')
    else:
        form = HelpRequestForm()
    return render(request, 'new_help_request.html', {'form': form})

def help_request_detail(request, pk):
    help_request = get_object_or_404(HelpRequest, pk=pk)
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.help_request = help_request
            response.save()
            return redirect('help_request_detail', pk=help_request.pk)
    else:
        form = ResponseForm()
    return render(request, 'help_request_detail.html', {'help_request': help_request, 'form': form})