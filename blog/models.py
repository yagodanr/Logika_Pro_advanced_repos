from django.db import models
from django.utils import timezone

# Create your models here.
    

class User(models.Model):
    login = models.CharField(max_length=127)
    email = models.EmailField()
    
    ROLE_CHOICES = {
        "AD": "admin",
        "US": "user"
    }
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default="user")

    def __str__(self) -> str:
        return self.login

class TimeStampMixin(models.Model): #https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        abstract = True


class Post(TimeStampMixin):
    title = models.CharField(max_length=127),
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Comment(TimeStampMixin):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
