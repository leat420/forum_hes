# src/urls.py
from django.contrib import admin
from django.urls import path

from src import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('opinions/', views.opinions, name='opinions'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comments/', views.display_comments, name='display_comments'),
    path('help_requests/', views.help_requests, name='help_requests'),
    path('help_requests/new/', views.new_help_request, name='new_help_request'),
    path('help_requests/<int:pk>/', views.help_request_detail, name='help_request_detail'),
    path('help_requests/<int:pk>/delete/', views.delete_help_request, name='delete_help_request'),
]
