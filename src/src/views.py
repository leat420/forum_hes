from datetime import datetime
from django.shortcuts import render

def index(request):
    date=datetime.today()

    return render(request, 'src/index.html', context={"prénom": "Arlinda", "date": date})