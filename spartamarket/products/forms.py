from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'price', 'address']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
