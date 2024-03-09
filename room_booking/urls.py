from django.urls import path, include
from .views import *



urlpatterns = [
    path("", get_rooms_list, name="rooms"),
    path("room/<int:pk>", get_room_detail, name="room_detail"),
    path("booking/", booking_form, name="booking_form"),
    path("booking/<int:pk>", booking_detail, name="booking_detail"),
    path("auth/", include("auth_system.urls"))
]
