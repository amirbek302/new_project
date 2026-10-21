from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils.http import url_has_allowed_host_and_scheme

from .models import Post, Like

# Create your views here.
def interesting(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'interesting.html', {'posts': posts,})


@login_required(login_url='login')
@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        like, created = Like.objects.get_or_create(
            user=request.user,
            post=post  # like
        )

        if not created:
            like.delete()  # Отмена Like

    next_url = request.POST.get('next', '')

    if next_url and url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure()
    ):
        return redirect(next_url)

    return redirect('interesting')