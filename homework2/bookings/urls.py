from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create router for API endpoints
router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'seats', views.SeatViewSet, basename='seat')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    
    # Template views
    path('', views.movie_list, name='movie_list'),
    path('book/<int:movie_id>/', views.seat_booking, name='book_seat'),
    path('history/', views.booking_history, name='booking_history'),
]