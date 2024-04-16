# products/urls.py
from django.urls import path
from .views import index_view, post_create_view, post_detail, product_update, product_delete

app_name = 'products' 

urlpatterns = [
    path('', index_view, name='index'),
    path('create/', post_create_view, name='post_create'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('update/<int:id>/', product_update, name='product_update'),
    path('delete/<int:id>/', product_delete, name='product_delete'),
]
