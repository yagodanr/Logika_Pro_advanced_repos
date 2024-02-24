from django.contrib import admin
from .models import *

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'capacity', 'location', 'description', )
    list_display_links = ("id", "number")

    search_fields = ('id', 'number')
    
    
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'user', 'from_time', 'to_time', 'created_at', )
    list_display_links = ("id", "room")

    search_fields = ('id', 'room', 'user')


admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
