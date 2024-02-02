from django.db import models

# Create your models here.
    

class User(models.Model):
    login = models.CharField(max_length=127)
    email = models.EmailField()
    
    ROLE_CHOICES = {
        "AD": "admin",
        "US": "user"
    }
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default="user")

class TimeStampMixin(models.Model): #https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampMixin):
    title = models.CharField(max_length=127),
    text = models.TextField()
    author = models.ForeignKey(User)

class Content(TimeStampMixin):
    text = models.TextField()
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    
