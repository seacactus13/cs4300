from rest_framework import serializers
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    """Serializer for Movie model"""
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'duration']


class SeatSerializer(serializers.ModelSerializer):
    """Serializer for Seat model"""
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'booking_status']


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model (for displaying booking info)"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    seat_number = serializers.CharField(source='seat.seat_number', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'movie', 'movie_title', 'seat', 'seat_number', 
                  'user', 'username', 'booking_date']
        read_only_fields = ['booking_date']
    
    def validate(self, data):
        """Validate that the seat is available"""
        seat = data.get('seat')
        movie = data.get('movie')
        
        if seat.booking_status == 'booked':
            raise serializers.ValidationError("This seat is already booked.")
        
        # Check if this seat is already booked for this movie
        if Booking.objects.filter(movie=movie, seat=seat).exists():
            raise serializers.ValidationError("This seat is already booked for this movie.")
        
        return data


class BookingCreateSerializer(serializers.ModelSerializer):
    """Simplified serializer for creating bookings"""
    class Meta:
        model = Booking
        fields = ['movie', 'seat', 'user']