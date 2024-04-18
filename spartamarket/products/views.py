# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Like
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Count

# products/views.py 수정
from django.db.models import Count

def index_view(request):
    posts_list = Post.objects.annotate(like_count=Count('like_entries')).order_by('-created_at')
    paginator = Paginator(posts_list, 9)  # 한 페이지 당 9개의 게시물

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'index.html', {'posts': posts})




def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    like_count = post.like_entries.count()
    return render(request, 'products/post_detail.html', {'post': post, 'like_count': like_count})


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

def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete() 
    return HttpResponseRedirect(reverse('products:post_detail', args=[post_id]))
