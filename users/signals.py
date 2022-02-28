import email
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


"""
    create profile on user registration and update user email and username on updating profile email and username

"""

def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(user=user, username=user.username, email=user.email)

post_save.connect(create_profile, sender=User)

def update_email_username(sender, instance, **kwargs):
    profile = instance
    # update email
    if profile.email != profile.user.email:
        profile.user.email = profile.email
        profile.user.save()
    # update username
    if profile.username != profile.user.username:
        profile.user.username = profile.username
        profile.user.save()
    pass

post_save.connect(update_email_username, sender=Profile)