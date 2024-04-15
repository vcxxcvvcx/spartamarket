# products/urls.py
from django.urls import path
from .views import product_list_view, product_detail_view, post_list_view, post_create_view, create_post

app_name = 'products' 

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<int:id>/', product_detail_view, name='product_detail'),
    path('create/', post_create_view, name='post_create'),
    path('create/', create_post, name='create_post'),
    path('posts/', post_list_view, name='post_list'), 
]
