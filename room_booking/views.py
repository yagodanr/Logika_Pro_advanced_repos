from django.shortcuts import render
from .models import *

# Create your views here.

def get_rooms_list(request):
    rooms = Room.objects.all()
    
    context = {
        "rooms" : rooms
    }
    
    return render(
        request,
        "room_booking/rooms_list.html",
        context
    )

