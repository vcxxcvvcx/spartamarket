# products/urls.py
from django.urls import path
from .views import index_view, post_create_view, post_detail, post_edit_view, product_delete, toggle_like

app_name = 'products' 

urlpatterns = [
    path('', index_view, name='index'),
    path('create/', post_create_view, name='post_create'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('post/edit/<int:id>/', post_edit_view, name='post_edit'),
    path('delete/<int:id>/', product_delete, name='product_delete'),
    path('post/<int:post_id>/toggle_like/', toggle_like, name='toggle_like'),
]
