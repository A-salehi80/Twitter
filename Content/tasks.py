# relation/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from Relation.models import Relation
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_daily_follower_posts():
    today = timezone.now().date()

    for user in User.objects.all():
        following_ids = Relation.objects.filter(follower=user).values_list('following_id', flat=True)
        todays_posts = Post.objects.filter(
            posted_by__in=following_ids,
            created_at__date=today
        ).select_related('posted_by')

        if not todays_posts.exists():
            continue

        post_lines = [f"{post.posted_by.phone}: {post.content}" for post in todays_posts]
        message_body = "\n\n".join(post_lines)

        send_mail(
            subject=f"Your daily feed - {today.strftime('%Y-%m-%d')}",
            message=message_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
