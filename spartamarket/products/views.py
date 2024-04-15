# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .models import Post
from .forms import PostForm

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

def post_list_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'products/post_list.html', {'posts': posts})

def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('products:post_list')
    else:
        form = PostForm()
    return render(request, 'products/post_create.html', {'form': form})
