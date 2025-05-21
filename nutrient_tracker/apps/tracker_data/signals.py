from apps.user_info.models import User
from apps.tracker_data.models import NutrientTracker
from apps.nutrient_data.models import Nutrient

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


@receiver(post_delete, sender=User)
def delete_nutrient_tracker(sender, instance, **kwargs):
    if instance.nutrient_tracker:
        instance.nutrient_tracker.all().delete()


@receiver(post_save, sender=User)
def create_nutrient_tracker(sender, instance, created, **kwargs):
    if created:

        nutrients = Nutrient.objects.all()
        NutrientTracker.objects.bulk_create(
            [
                NutrientTracker(
                    user=instance, date=instance.date_joined, nutrient=nutrient
                )
                for nutrient in nutrients
            ]
        )
        # instance.save()
    print("tried to create some nutrient trackers")
