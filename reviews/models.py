from django.db import models

# Create your models here.

class Review(models.Model):

    username = models.CharField(max_length=255)
    text =  models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = ("Review")
        verbose_name_plural = ("Reviews")

    def __str__(self):
        return self.username


