# src/urls.py
from django.contrib import admin
from django.urls import path

from src import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('opinions/', views.opinions, name='opinions'),
    path('question_reponses/', views.question_reponses, name='question_reponses'),
]
