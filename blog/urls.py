from django.urls import path

from .views import *

urlpatterns = [
    path("", get_all_posts, name="get_posts"),
    path("post/<int:post_id>", get_post_by_id, name="get_post"),
    path("author/<int:author_id>", get_author_by_id, name="get_author")
]


