# spartamarket/views.py
from django.shortcuts import render
from products.models import Post


from django.core.paginator import Paginator

def index_view(request):
    posts_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 9)  # Show 9 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'index.html', {'posts': posts})