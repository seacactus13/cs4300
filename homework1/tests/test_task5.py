import sys
import os
sys.path.insert(0, os.path.abspath("../src"))

import task5

def test_favorite_books():
    books, first_three = task5.favorite_books()
    assert len(books) == 5
    assert len(first_three) == 3
    assert first_three[0]["title"] == "1984"
    assert first_three[1]["title"] == "Shoe Dog"
    assert first_three[2]["title"] == "The Great Gatsby"

def test_student_database():
    students = task5.student_database()
    assert students["Alice"] == "ID001"
    assert students["Bob"] == "ID002"
    assert "Charlie" in students
    assert len(students) == 4
