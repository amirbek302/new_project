from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from posts.models import Post
from posts.forms import PostForm
from register.models import User

@login_required(login_url='login')
def room(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('room')
    else:
        post_form = PostForm()

    posts = Post.objects.filter(
        author=request.user
    ).order_by('-created_at')

    return render(request, 'room.html', {
        'post_form': post_form,
        'posts': posts,
    })


@login_required(login_url='login')
@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    post.delete()

    return redirect('room')

# /////////////\guest_room\//////////////
def guest_room(request, username):
    profile_user = get_object_or_404(
        User,
        username=username
    )

    if request.user.is_authenticated and request.user == profile_user:
        return redirect('room')

    posts = Post.objects.filter(author=profile_user).order_by('-created_at')

    return render(request, 'guest_room.html', {
        'profile_user': profile_user,
        'posts': posts,
    })