# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse

def index_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'products/post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('products:index')
    else:
        form = PostForm()
    return render(request, 'products/post_create.html', {'form': form})


def post_edit_view(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('products:post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'products/post_edit.html', {'form': form, 'post': post})


def product_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('products:index')
