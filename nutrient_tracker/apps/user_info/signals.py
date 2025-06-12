from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.user_info.models import User, Profile

# send a signal for when an action is performed

# style:

# @receiver(signal_flag, sender=NameOfModel)
# def action_performed(sender, instance, created, **kwargs):
#     additional logic

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """create a profile when a user is created"""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """save a profile when a user is saved"""
    instance.profile.save()