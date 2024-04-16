# spartamarket/views.py
from django.shortcuts import render
from products.models import Post


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})
 
