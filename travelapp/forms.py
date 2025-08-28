from django import forms 
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','phone','address','email']



class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['travel_option','number_of_seats',]