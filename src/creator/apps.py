from django.apps import AppConfig


class CreatorConfig(AppConfig):
    """
    Класс конфигурации приложения "Сздатель".
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "creator"
    verbose_name = "Создатель"
