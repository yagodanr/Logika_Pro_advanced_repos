from django.shortcuts import render
from .models import *

# Create your views here.

def get_all_posts(request):
    posts = Post.objects.all()
    
    
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

