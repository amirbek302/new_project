from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'What’s new with you?',
                'rows': 4,
                'maxlength': 500,
            })
        }