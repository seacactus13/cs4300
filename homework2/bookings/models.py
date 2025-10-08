from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    """Model representing a movie in the theater"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    
    class Meta:
        ordering = ['release_date']
    
    def __str__(self):
        return self.title


class Seat(models.Model):
    """Model representing a seat in the theater"""
    SEAT_STATUS_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
    ]
    
    seat_number = models.CharField(max_length=10, unique=True)
    booking_status = models.CharField(
        max_length=20,
        choices=SEAT_STATUS_CHOICES,
        default='available'
    )
    
    class Meta:
        ordering = ['seat_number']
    
    def __str__(self):
        return f"Seat {self.seat_number} - {self.booking_status}"


class Booking(models.Model):
    """Model representing a booking"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='bookings')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-booking_date']
        unique_together = ['movie', 'seat']  # Prevent double booking
    
    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - Seat {self.seat.seat_number}"
    
    def save(self, *args, **kwargs):
        """Override save to update seat status"""
        self.seat.booking_status = 'booked'
        self.seat.save()
        super().save(*args, **kwargs)