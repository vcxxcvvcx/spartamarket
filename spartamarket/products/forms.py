from django import forms
from .models import Post
from .models import Product

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'price', 'address']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']