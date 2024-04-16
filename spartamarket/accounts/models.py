#account/models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from products.models import Post

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    favorites = models.ManyToManyField(Post, related_name='favorited_by_users')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}의 프로필'

class Follow(models.Model):
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)  # 팔로우 받는 사람
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)  # 팔로우 하는 사람
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('following', 'follower')

    def __str__(self):
        return f'{self.follower.username} -> {self.following.username}'


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='favorited_by', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
