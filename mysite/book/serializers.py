from rest_framework import serializers
from .models import Hotel, Room, Booking


class HotelSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name_hotel', 'description', 'address', 'city', 'country']


class RoomSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"