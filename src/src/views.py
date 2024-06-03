from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment
from django.shortcuts import render, get_object_or_404, redirect
from .forms import HelpRequestForm, ResponseForm
from .models import HelpRequest
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

def help_requests(request):
    requests = HelpRequest.objects.all().order_by('-created_at')
    form= ResponseForm() #formulaire de réponse
    return render(request, 'help_requests.html', {'requests': requests, 'form': form})

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
def delete_help_request(request, pk):
    help_request = get_object_or_404(HelpRequest, pk=pk)
    if request.method == 'POST':
        help_request.delete()
        return redirect('help_requests')
    return render(request, 'delete_help_request.html', {'help_request': help_request})

def delete_help_request(request, pk):
    help_request = get_object_or_404(HelpRequest, pk=pk)
    if request.method == 'POST':
        help_request.delete()
        return redirect('help_requests')
    return render(request, 'delete_help_request.html', {'help_request': help_request})