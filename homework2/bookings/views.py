from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Seat, Booking
from .serializers import (
    MovieSerializer, SeatSerializer, BookingSerializer, 
    BookingCreateSerializer
)


# ============== API ViewSets ==============

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    """
    API endpoint for seat availability and booking
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get all available seats"""
        available_seats = Seat.objects.filter(booking_status='available')
        serializer = self.get_serializer(available_seats, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def book(self, request, pk=None):
        """Book a specific seat"""
        seat = self.get_object()
        if seat.booking_status == 'booked':
            return Response(
                {'error': 'Seat already booked'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        seat.booking_status = 'booked'
        seat.save()
        return Response({'message': 'Seat booked successfully'})


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for booking operations
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
            return BookingCreateSerializer
        return BookingSerializer
    
    @action(detail=False, methods=['get'])
    def my_bookings(self, request):
        """Get bookings for the current user"""
        user_id = request.query_params.get('user_id')
        if user_id:
            bookings = Booking.objects.filter(user_id=user_id)
            serializer = self.get_serializer(bookings, many=True)
            return Response(serializer.data)
        return Response(
            {'error': 'user_id parameter required'},
            status=status.HTTP_400_BAD_REQUEST
        )


# ============== Template Views ==============

def movie_list(request):
    """Display list of all movies"""
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking(request, movie_id):
    """Display seat booking page for a specific movie"""
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()
    
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id=seat_id)
        
        if seat.booking_status == 'booked':
            messages.error(request, 'This seat is already booked!')
        else:
            # Create booking (requires logged-in user)
            if request.user.is_authenticated:
                booking = Booking.objects.create(
                    movie=movie,
                    seat=seat,
                    user=request.user
                )
                messages.success(request, f'Successfully booked seat {seat.seat_number}!')
                return redirect('booking_history')
            else:
                messages.error(request, 'Please log in to book a seat.')
                return redirect('login')
    
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })


def booking_history(request):
    """Display booking history for the current user"""
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
    else:
        bookings = []
    
    return render(request, 'bookings/booking_history.html', {
        'bookings': bookings
    })