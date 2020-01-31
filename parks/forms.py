from django import forms
from .models import Park, Comment

class ParkForm(forms.ModelForm):

    class Meta:
        model = Park
        fields = ('name', 'state', 'description', 'photo_url')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('park','author', 'title', 'body')