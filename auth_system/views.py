from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from auth_system.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
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
        
        
def log(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user=user)
                return redirect("rooms")
            else:
                messages.error(request, "Wrong login or password")

    else:
        form = AuthenticationForm()
        
        return render(
            request,
            "auth_system/login.html",
            context={"form": form}
        )
        
