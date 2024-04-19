# accounts/views.py
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Follow
from products.models import Post, Like
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('index')
        else:
            return render(request, 'accounts/register.html', {'form': form, 'error': 'Please check your input.'})
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    posts = user.posts.all()  
    favorites = Post.objects.filter(like_entries__user=user)  
    followers = user.followers.count() 
    following = user.following.count()  

    return render(request, 'accounts/profile.html', {
        'user': user,
        'posts': posts,
        'favorites': favorites,
        'followers': followers,
        'following': following
    })


@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(get_user_model(), username=username)
    if request.user != user_to_follow:
        follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        if not created:
            follow.delete()  
    return redirect('accounts:user_profile', username=username)