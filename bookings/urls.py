from django.urls import path
from .views import BookingListCreateView

urlpatterns = [
    path('book/', BookingListCreateView.as_view(), name='book_car'),
]