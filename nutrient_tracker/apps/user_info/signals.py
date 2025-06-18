from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.user_info.models import User, Profile, Favorite, History, TrackedNutrients

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


@receiver(post_save, sender=User)
def create_favorites(sender, instance, created, **kwargs):
    """create a favorite when a user is created"""
    if created:
        Favorite.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_favorites(sender, instance, **kwargs):
    """save a favorite when a user is saved"""
    instance.favorite.save()


@receiver(post_save, sender=User)
def create_history(sender, instance, created, **kwargs):
    """create a history when a user is created"""
    if created:
        History.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_history(sender, instance, **kwargs):
    """save a history when a user is saved"""
    instance.history.save()


@receiver(post_save, sender=User)
def create_tracked_nutrients(sender, instance, created, **kwargs):
    """create a tracked_nutrients when a user is created"""
    if created:
        TrackedNutrients.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_tracked_nutrients(sender, instance, **kwargs):
    """save a tracked_nutrients when a user is saved"""
    instance.trackednutrients.save()
