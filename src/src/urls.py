# src/urls.py
from django.contrib import admin
from django.urls import path

from src import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('opinions/', views.opinions, name='opinions'),
    path('question_reponses/', views.question_reponses, name='question_reponses'),
    path('help_requests/', views.help_requests, name='help_requests'),
    path('help_requests/new/', views.new_help_request, name='new_help_request'),
    path('help_requests/<int:pk>/', views.help_request_detail, name='help_request_detail'),
]
