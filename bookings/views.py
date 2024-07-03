from .serializers import BookingSerializer
from rest_framework import generics
from .models import Booking


class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def perform_create(self, serializer):
        serializer.save()
