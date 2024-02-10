from django.shortcuts import render
from .models import *

# Create your views here.

def get_all_posts(request):
    posts = Post.objects.all()
    for post in posts:
        post.time_dif = post.published_recently()
    
    
    context = {
        "posts": posts,
        
    }
    return render(
        request,
        "blog/get_posts.html",
        context
    )
    
def get_post_by_id(request, post_id: int):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    
    return render(
        request,
        "blog/get_post_by_id.html",
        context,
    )
    
def get_author_by_id(request, author_id: int):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "posts": author.posts.all()
    }
    
    return render(
        request,
        "blog/get_author_by_id.html",
        context,
    )

