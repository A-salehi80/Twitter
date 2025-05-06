from django.db.models.signals import post_save
from django.dispatch import receiver
from User.models import User, Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    profile = Profile(user=instance)
    profile.save()