from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Post, Like

# Create your views here.
def interesting(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'interesting.html', {'posts': posts,})


@login_required(login_url='login')
@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author == request.user:
        return redirect('interesting')

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )  # Like

    if not created:
        like.delete()    # Отмена Like

    return redirect('interesting')