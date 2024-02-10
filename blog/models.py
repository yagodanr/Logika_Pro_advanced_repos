from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    
    
    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Зміст")
    published_date = models.DateTimeField(default=timezone.now, editable=True, verbose_name="Дата створення")

    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name="posts", verbose_name="Автор")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"
        ordering = ["published_date"]
    
    
    def published_recently(self):
        
        return self.published_date >= timezone.now() - timedelta(days=7)


