from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.user_info.models import User
from apps.tracker_data.models import NutrientTracker
from apps.nutrient_data.models import Nutrient


@receiver(post_save, sender=User)
def create_nutrient_tracker(sender, instance, created, **kwargs):
    # if created:
    #     if not instance.nutrient_tracker:
    #         nutrients = Nutrient.objects.all()
    #         instance.nutrient_tracker = NutrientTracker.objects.bulk_create(
    #             [
    #                 # NutrientTracker(date=instance.date_joined, nutrient_range=nutrient) for every nutrient
    #             ]
    #             # NutrientTracker(date=instance.date_joined, nutrient_range=nutrient)
    #             # for nutrient in nutrients
    #         )
    pass

# merge nutrient_tracker and nutrient_range to simplify creation process