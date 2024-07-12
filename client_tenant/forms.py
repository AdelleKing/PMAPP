from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': ''
        }
        widgets = {
            'text': forms.Textarea(attrs={
                "rows": 3,
                'class': "font1 text-1xl bg-gray-100 p-2",
                'placeholder': 'add comment here...',
                'style': 'resize: none; width: 100%; border:solid; border-width:.5px; border-radius:9px'
            }),
        }
