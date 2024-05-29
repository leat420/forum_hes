from django import forms
from .models import Comment
from django import forms
from .models import HelpRequest, Response


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['subject_name', 'subject_field', 'creator_name', 'question']
        widgets = {
            'subject_field': forms.Select(choices=[('Math', 'Math'), ('Science', 'Science'), ('History', 'History')]),
        }

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['responder_name', 'answer']