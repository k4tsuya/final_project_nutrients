from django.db.models.signals import post_save
from django.dispatch import receiver

# add a signal for when an action is performed

# style:

# @receiver(signal_flag, sender=NameOfModel)
# def action_performed(sender, instance, created, **kwargs):
#     additional logic
