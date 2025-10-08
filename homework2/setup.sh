#!/bin/bash

# Movie Theater Booking Application Setup Script
# This script automates the setup process for the Django application

echo "🎬 Movie Theater Booking Application Setup"
echo "==========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "myenv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv myenv --system-site-packages
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source myenv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install django djangorestframework

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Check if superuser exists
echo ""
echo "👤 Admin User Setup"
echo "-------------------"
read -p "Do you want to create a superuser? (y/n): " create_user

if [ "$create_user" = "y" ] || [ "$create_user" = "Y" ]; then
    python manage.py createsuperuser
fi

# Load sample data
echo ""
read -p "Do you want to load sample data? (y/n): " load_data

if [ "$load_data" = "y" ] || [ "$load_data" = "Y" ]; then
    echo "📊 Loading sample data..."
    python manage.py shell << EOF
from bookings.models import Movie, Seat
from datetime import date

# Create movies
movies_created = 0
if Movie.objects.count() == 0:
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
    Movie.objects.create(
        title="Interstellar",
        description="A team of explorers travel through a wormhole in space.",
        release_date=date(2024, 3, 10),
        duration=169
    )
    movies_created = 3
    print(f"✅ Created {movies_created} movies")
else:
    print("ℹ️  Movies already exist, skipping...")

# Create seats
seats_created = 0
if Seat.objects.count() == 0:
    rows = ['A', 'B', 'C', 'D', 'E']
    for row in rows:
        for num in range(1, 11):
            Seat.objects.create(seat_number=f"{row}{num}")
            seats_created += 1
    print(f"✅ Created {seats_created} seats")
else:
    print("ℹ️  Seats already exist, skipping...")

EOF
    echo "✅ Sample data loaded successfully"
fi

# Run tests
echo ""
read -p "Do you want to run tests? (y/n): " run_tests

if [ "$run_tests" = "y" ] || [ "$run_tests" = "Y" ]; then
    echo "🧪 Running tests..."
    python manage.py test
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the development server, run:"
echo "   python manage.py runserver 0.0.0.0:3000"
echo ""
echo "📱 Access the application at:"
echo "   Web UI: http://localhost:3000/"
echo "   API: http://localhost:3000/api/"
echo "   Admin: http://localhost:3000/admin/"
echo ""