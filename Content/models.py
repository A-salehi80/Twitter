from django.db import models
from User.models import User


class Postable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message=models.TextField(blank=True, null=True)


class Post(Postable):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Like(Postable):
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    on_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
