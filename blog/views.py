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

