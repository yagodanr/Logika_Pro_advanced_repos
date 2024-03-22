from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from auth_system.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
        
            return redirect("rooms")
        
        else:
            messages.error(request, message="Registration error")
        
        
    else:
        form = CustomUserCreationForm()
        
        return render(
            request,
            "auth_system/register.html",
            context={"form": form}
        )
        
        
def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            login(request, user=user)
            next_url = request.GET.get("next")
            if next_url is None:
                next_url = ""
            
            return redirect(next_url)
        else:
            next_url = request.GET.get("next")
            if next_url is None:
                next_url = "/"
            
            return render(
                request,
                "auth_system/login.html",
                context={"form": form, "next_url": next_url}
            )

    else:
        form = AuthenticationForm()
        
        next_url = request.GET.get("next")
        if next_url is None:
            next_url = "/"
        
        return render(
            request,
            "auth_system/login.html",
            context={"form": form, "next_url": next_url}
        )
        
def log_out(request):
    if request.method == "POST":
        logout(request)

        next_url = request.GET.get("next")
        if next_url == "/":
            next_url = "login"
        return redirect(next_url)
        
    else:
        next_url = request.GET.get("next")
        if next_url is None:
            next_url = "/"
        
        return render(
            request,
            "auth_system/logout.html",
            context={"next_url": next_url}
        )
        
