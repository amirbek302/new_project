from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.text[:30]}'

class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(     # запрещает одному пользователю поставить много Like
                fields=['user', 'post'],
                name='unique_user_post_like'
            )
        ]