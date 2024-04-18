# spartamarket/views.py
from django.shortcuts import render
from products.models import Post


from django.core.paginator import Paginator
from django.db.models import Count

def index_view(request):
    posts_list = Post.objects.annotate(like_count=Count('like_entries')).order_by('-created_at')
    paginator = Paginator(posts_list, 9)  
    
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'index.html', {'posts': posts})