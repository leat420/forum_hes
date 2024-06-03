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
        fields = ['Branche', 'Thème', 'Prénom', 'Question']
        widgets = {
            'Branche': forms.Select(choices=[('Biologie', 'Biologie'), ('Chimie', 'Chimie'), ('Informatique', 'Informatique'), ('Mathématiques', 'Mathématiques')]),
        }

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['responder_name', 'answer']