# src/urls.py
from django.contrib import admin
from django.urls import path

from src import views
from .views import delete_question

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('opinions/', views.opinions, name='opinions'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comments/', views.display_comments, name='display_comments'),
    path('question/new/', views.create_question, name='create_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/delete/<int:question_id>/', delete_question, name='delete_question'),
]
