from django.apps import AppConfig


class UserInfoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user_info"
    verbose_name = "User Info"

    def ready(self):
        """Signal registration"""
        import apps.user_info.signals
