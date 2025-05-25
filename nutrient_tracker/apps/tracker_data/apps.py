from django.apps import AppConfig


class TrackerDataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.tracker_data"
    verbose_name = "Tracker Data"

    def ready(self):
        import apps.tracker_data.signals