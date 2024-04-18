from django.contrib import admin
from .models import Post
from .models import Like

# Product와 Post 모델을 관리자 페이지에서 볼 수 있도록 등록

admin.site.register(Post)
admin.site.register(Like)
