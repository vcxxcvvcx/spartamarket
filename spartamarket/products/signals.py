from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like, Post

# Like 인스턴스 생성 후 호출
@receiver(post_save, sender=Like)
def increment_likes_count(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        post.likes_count += 1
        post.save()

# Like 인스턴스 삭제 후 호출
@receiver(post_delete, sender=Like)
def decrement_likes_count(sender, instance, **kwargs):
    post = instance.post
    post.likes_count -= 1
    post.save()
