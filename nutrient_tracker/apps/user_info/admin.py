from typing import ClassVar

from django.contrib import admin

from .models import Favorite, History, User, TrackedNutrients

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


class CustomFavoriteAdmin(admin.ModelAdmin):
    list_display: ClassVar[list] = [
        "user",
    ]

    fieldsets = (
        (
            "Account info",
            {
                "fields": (
                    "user",
                    "ingredient",
                    "recipe",
                    "nutrient",
                ),
            },
        ),
    )


class CustomHistoryAdmin(admin.ModelAdmin):
    list_display: ClassVar[list] = [
        "user",
    ]

    fieldsets = (
        (
            "Account info",
            {
                "fields": (
                    "user",
                    "ingredient",
                    "recipe",
                    "nutrient",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Favorite, CustomFavoriteAdmin)
admin.site.register(History, CustomHistoryAdmin)
admin.site.register(
    TrackedNutrients,
)
