from django.urls import path

from .views import *

urlpatterns = [
    path("", get_all_posts, name="get_posts")
]


