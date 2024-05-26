from django.shortcuts import render
# Create your views here.
def index(request):
    print("le blog")
    return render(request, 'blog/index.html')