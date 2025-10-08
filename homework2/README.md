# Movie Theater Booking Application

A RESTful movie theater booking application built with Django and Django REST Framework. Users can view movie listings, book seats, and check their booking history through both a web interface and REST API.

## 🎬 Features

- **Movie Listings**: Browse available movies with details
- **Seat Booking**: Interactive seat selection with real-time availability
- **Booking History**: View all your past and upcoming bookings
- **REST API**: Full CRUD operations via RESTful endpoints
- **Responsive UI**: Bootstrap-based attractive interface
- **Admin Panel**: Django admin for managing movies, seats, and bookings

## 🛠️ Technology Stack

- **Backend**: Python 3.x, Django 4.x
- **API**: Django REST Framework
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (default)

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone or Navigate to Project

```bash
cd homework2/movie_theater_booking
```

### 2. Create Virtual Environment

```bash
python3 -m venv myenv --system-site-packages
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django djangorestframework
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin Access)

```bash
python manage.py createsuperuser
# Follow prompts to set username, email, and password
```

### 6. Create Sample Data

```bash
python manage.py shell
```

Then in the Python shell:

```python
from bookings.models import Movie, Seat
from datetime import date

# Create movies
Movie.objects.create(
    title="Inception",
    description="A thief who steals corporate secrets through dream-sharing technology.",
    release_date=date(2024, 1, 15),
    duration=148
)

Movie.objects.create(
    title="The Dark Knight",
    description="When the menace known as the Joker wreaks havoc on Gotham.",
    release_date=date(2024, 2, 20),
    duration=152
)

# Create seats (A1-A5, B1-B5, C1-C5)
rows = ['A', 'B', 'C']
for row in rows:
    for num in range(1, 6):
        Seat.objects.create(seat_number=f"{row}{num}")

exit()
```

### 7. Run Development Server

```bash
python manage.py runserver 0.0.0.0:3000
```

Visit: `http://localhost:3000` or your DevEdu app URL

## 📁 Project Structure

```
movie_theater_booking/
├── bookings/
│   ├── migrations/
│   ├── templates/
│   │   └── bookings/
│   │       ├── base.html
│   │       ├── movie_list.html
│   │       ├── seat_booking.html
│   │       └── booking_history.html
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── movie_theater_booking/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## 🔌 API Endpoints

### Movies
- `GET /api/movies/` - List all movies
- `POST /api/movies/` - Create a new movie
- `GET /api/movies/{id}/` - Get movie details
- `PUT /api/movies/{id}/` - Update a movie
- `DELETE /api/movies/{id}/` - Delete a movie

### Seats
- `GET /api/seats/` - List all seats
- `GET /api/seats/available/` - List available seats only
- `POST /api/seats/{id}/book/` - Book a specific seat

### Bookings
- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/` - Create a new booking
- `GET /api/bookings/my_bookings/?user_id={id}` - Get user's bookings

## 🧪 Testing

Run all tests:

```bash
python manage.py test
```

Run specific test class:

```bash
python manage.py test bookings.tests.MovieModelTest
```

Run with verbosity:

```bash
python manage.py test --verbosity=2
```

## 🎨 Web Interface Routes

- `/` - Movie listings page
- `/book/{movie_id}/` - Seat booking page
- `/history/` - User's booking history
- `/admin/` - Django admin panel

## 📊 Sample API Requests

### Create a Booking (POST)

```bash
curl -X POST http://localhost:3000/api/bookings/ \
  -H "Content-Type: application/json" \
  -d '{
    "movie": 1,
    "seat": 1,
    "user": 1
  }'
```

### Get Available Seats (GET)

```bash
curl http://localhost:3000/api/seats/available/
```

### Get Movie List (GET)

```bash
curl http://localhost:3000/api/movies/
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

### Migration Issues
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

## 👥 Contributing

This is a homework assignment project. For educational purposes only.

## 📝 AI Usage Declaration

This project was developed with assistance from Claude AI for:
- Code structure and Django best practices
- Bootstrap template design
- API endpoint implementation
- Test case development
- Documentation formatting

All code was reviewed, tested, and customized for the specific requirements of this assignment.

## 📄 License

This project is for educational purposes as part of CS4300/5300 coursework.

## 👨‍💻 Author

Enzo Knapp 
CS4300/5300 - Homework 2  
University of Colorado Colorado Springs