from typing import ClassVar

from django.contrib import admin

from .models import Favorite, History, User

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display: ClassVar[list] = [
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
        "gender",
        "is_active",
        "is_staff",
        "is_superuser",
    ]

    fieldsets = (
        (
            "Account info",
            {
                "fields": (
                    "username",
                    "password",
                    "email",
                    "role",
                ),
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "gender",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
