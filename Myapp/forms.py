from django import forms
from .models import Post

class JokeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content']