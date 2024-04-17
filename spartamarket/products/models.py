from django.db import models
from django.contrib.auth.models import User
# from products.models import Post
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image_url = models.URLField(default='', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    address = models.CharField(max_length=255)
    likes_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_posts')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_entries')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'