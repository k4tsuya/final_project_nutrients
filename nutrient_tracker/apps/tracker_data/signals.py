from apps.user_info.models import User
from apps.tracker_data.models import NutrientRange

from django.db.models.signals import post_delete
from django.dispatch import receiver


@receiver(post_delete, sender=NutrientRange)
def delete_nutrient_range(sender, instance, **kwargs):
    if instance.nutrient_range:
        instance.nutrient_range.delete()


@receiver(post_delete, sender=User)
def delete_nutrient_tracker(sender, instance, **kwargs):
    if instance.nutrient_tracker:
        instance.nutrient_tracker.delete()
