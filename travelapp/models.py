from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    email=models.EmailField()

    def __str__(self):
        return f"{self.user.username} profile"

class TravelOption(models.Model):
    TRAVEL_TYPES = [
        ("flight", "Flight"),
        ("train", "Train"),
        ("bus", "Bus"),
    ]

    travel_id = models.AutoField(primary_key=True)  
    type = models.CharField(max_length=10, choices=TRAVEL_TYPES)  
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.get_type_display()} from {self.source} to {self.destination} on {self.date_time}"
    



class Booking(models.Model):
    STATUS_CHOICES = [
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    ]

    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    travel_option = models.ForeignKey(TravelOption, on_delete=models.CASCADE, related_name="bookings")
    number_of_seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Confirmed")

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.travel_option.price * self.number_of_seats
        super().save(*args, **kwargs)