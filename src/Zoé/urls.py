from views import comment_form
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('comment-form/', comment_form, name='comment-form'),
    path('admin/', admin.site.urls),
    path('mon-app/', include('mon_app.urls')),
    # Autres URLs de ton application
]
