"""
Функции панели управления для приложения "Автор".
"""

from django.contrib import admin
from creator.models import Creator


@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = (
        "github_url",
        "resume_url",
        "email",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "github_url",
        "resume_url",
        "email",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
