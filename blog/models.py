from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Зміст")
    published_date =models.DateTimeField(default=timezone.now, editable=False, verbose_name="Дата створення")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"
        ordering = ["published_date"]
