from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


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


def get_room_detail(request, pk: int):
    room = Room.objects.get(id=pk)
    
    context = {
        "room" : room
    }
    
    return render(
        request,
        "room_booking/room_detail.html",
        context
    )
    

@login_required
def booking_form(request):
    
    if request.method == "GET": 
        return render(
            request,
            "room_booking/booking_form.html"
        )
        
    elif request.method == "POST":
        room_number = request.POST.get("room_number")
        from_time = request.POST.get("from_time")
        to_time = request.POST.get("to_time")
        
        try: 
            room = Room.objects.get(number=room_number)    
        except ValueError:
            return HttpResponse("Wrong room_number", status=400)
        except Room.DoesNotExist:
            return HttpResponse("Room does not exist", status=404)
        
        booking = Booking.objects.create(
            room=room,
            user=request.user,
            from_time=from_time,
            to_time=to_time
        )
        
        return redirect("booking_detail", pk=booking.id)
        
        
        
        
@login_required
def booking_detail(request, pk: int):
    booking = Booking.objects.get(id=pk)
    
    if(request.user != booking.user):
        return redirect("rooms")
    
    context = {
        "booking": booking
    }
    
    return render(
        request,
        "room_booking/booking_detail.html",
        context
    )