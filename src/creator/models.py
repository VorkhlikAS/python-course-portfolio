from django.db import models
from base.models import TimeStampMixin


class Creator(TimeStampMixin):
    """
    Модель для хранения данных о создателе
    """

    github_url = models.URLField(verbose_name="Ссылка github")
    resume_url = models.URLField(verbose_name="Ссылка на резюме")
    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = "Информация о создателе"
        verbose_name_plural = "Информация о создателе"

    def __str__(self) -> str:
        return f"Объект 'создатель' (id={self.pk})"
