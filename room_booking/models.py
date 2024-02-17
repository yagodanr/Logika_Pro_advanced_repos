from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Room(models.Model):
    number = models.CharField(max_length=255)
    capacity = models.IntegerField()
    location = models.TextField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.id}, {self.number}"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")

    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user} : {self.room}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-from_time", "room", "user"]
    
    
