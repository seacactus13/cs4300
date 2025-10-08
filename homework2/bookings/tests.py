from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date
from .models import Movie, Seat, Booking


class MovieModelTest(TestCase):
    """Test cases for Movie model"""
    
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            release_date=date(2024, 1, 1),
            duration=120
        )
    
    def test_movie_creation(self):
        """Test that a movie is created correctly"""
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.duration, 120)
        self.assertIsInstance(self.movie, Movie)
    
    def test_movie_str(self):
        """Test the string representation of movie"""
        self.assertEqual(str(self.movie), "Test Movie")


class SeatModelTest(TestCase):
    """Test cases for Seat model"""
    
    def setUp(self):
        self.seat = Seat.objects.create(
            seat_number="A1",
            booking_status="available"
        )
    
    def test_seat_creation(self):
        """Test that a seat is created correctly"""
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertEqual(self.seat.booking_status, "available")
    
    def test_seat_str(self):
        """Test the string representation of seat"""
        expected = "Seat A1 - available"
        self.assertEqual(str(self.seat), expected)


class BookingModelTest(TestCase):
    """Test cases for Booking model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test description",
            release_date=date(2024, 1, 1),
            duration=120
        )
        self.seat = Seat.objects.create(
            seat_number="A1",
            booking_status="available"
        )
    
    def test_booking_creation(self):
        """Test that a booking is created correctly"""
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
        self.assertEqual(booking.movie, self.movie)
        self.assertEqual(booking.seat, self.seat)
        self.assertEqual(booking.user, self.user)
    
    def test_booking_updates_seat_status(self):
        """Test that creating a booking updates seat status"""
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
        self.seat.refresh_from_db()
        self.assertEqual(self.seat.booking_status, "booked")
    
    def test_booking_str(self):
        """Test the string representation of booking"""
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
        expected = f"testuser - Test Movie - Seat A1"
        self.assertEqual(str(booking), expected)


class MovieAPITest(APITestCase):
    """Test cases for Movie API endpoints"""
    
    def setUp(self):
        self.movie = Movie.objects.create(
            title="API Test Movie",
            description="Test description",
            release_date=date(2024, 1, 1),
            duration=120
        )
    
    def test_get_movies_list(self):
        """Test retrieving list of movies"""
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_get_movie_detail(self):
        """Test retrieving a single movie"""
        response = self.client.get(f'/api/movies/{self.movie.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "API Test Movie")
    
    def test_create_movie(self):
        """Test creating a new movie via API"""
        data = {
            'title': 'New Movie',
            'description': 'New description',
            'release_date': '2024-12-31',
            'duration': 150
        }
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)


class SeatAPITest(APITestCase):
    """Test cases for Seat API endpoints"""
    
    def setUp(self):
        self.seat1 = Seat.objects.create(
            seat_number="A1",
            booking_status="available"
        )
        self.seat2 = Seat.objects.create(
            seat_number="A2",
            booking_status="booked"
        )
    
    def test_get_seats_list(self):
        """Test retrieving list of seats"""
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_get_available_seats(self):
        """Test retrieving only available seats"""
        response = self.client.get('/api/seats/available/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['seat_number'], 'A1')


class BookingAPITest(APITestCase):
    """Test cases for Booking API endpoints"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="apiuser",
            password="testpass123"
        )
        self.movie = Movie.objects.create(
            title="API Movie",
            description="Test",
            release_date=date(2024, 1, 1),
            duration=120
        )
        self.seat = Seat.objects.create(
            seat_number="B1",
            booking_status="available"
        )
    
    def test_create_booking(self):
        """Test creating a booking via API"""
        data = {
            'movie': self.movie.id,
            'seat': self.seat.id,
            'user': self.user.id
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
    
    def test_cannot_book_booked_seat(self):
        """Test that booking a booked seat fails"""
        # Create first booking
        Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
        
        # Try to book the same seat
        user2 = User.objects.create_user(username="user2", password="pass")
        data = {
            'movie': self.movie.id,
            'seat': self.seat.id,
            'user': user2.id
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)