from rest_framework import viewsets, permissions
from .serializers import HotelSeriaLizer, RoomSeriaLizer, BookingSeriaLizer
from .models import Hotel, Room, Booking
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import RoomFilter


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSeriaLizer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['city', 'country']
    search_fields = ['name_hotel']
    permission_classes = [permissions.IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSeriaLizer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSeriaLizer