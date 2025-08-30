from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Booking
        fields="__all__"

         

class BookingGetSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Booking
        fields='__all__'