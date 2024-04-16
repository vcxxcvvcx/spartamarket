# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Follow,Favorite
from products.models import Post

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
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    if not hasattr(user, 'profile'):
        # 프로필이 존재하지 않는 경우, 생성합니다.
        Profile.objects.create(user=user)

    posts = user.posts.all()  # 유저가 등록한 물품
    favorites = user.profile.favorites.all()  # 유저가 찜한 물품
    followers = user.followers.count()  # 해당 유저를 팔로우하는 사용자 수
    following = user.following.count()  # 해당 유저가 팔로우하는 사용자 수

    return render(request, 'accounts/profile.html', {
        'user': user,
        'posts': posts,
        'favorites': favorites,
        'followers': followers,
        'following': following
    })

