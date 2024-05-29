from django.shortcuts import render
from forms import CommentForm


def comment_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige vers une page de confirmation ou une autre vue
    else:
        form = CommentForm()
    return render(request, 'mon_app/comment_form.html', {'form': form})
