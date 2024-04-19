#account/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    favorites = models.ManyToManyField('products.Post', related_name='favorited_by_profiles')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}의 프로필'

class Follow(models.Model):
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('following', 'follower')

    def __str__(self):
        return f'{self.follower.username} -> {self.following.username}'

# class Favorite(models.Model):
#     user = models.ForeignKey('auth.User', related_name='favorites', on_delete=models.CASCADE)
#     post = models.ForeignKey('products.Post', related_name='post_favorited_by', on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('user', 'post')

#     def __str__(self):
#         return f"{self.user.username} likes post {self.post_id}"
