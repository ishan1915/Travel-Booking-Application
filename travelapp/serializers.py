from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class UserCreateSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,style={'input_type':'password'})
    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self,validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user




class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Booking
        fields="__all__"

         

class BookingGetSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Booking
        fields='__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'