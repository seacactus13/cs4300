def favorite_books():
    books = [
        {"title": "1984", "author": "George Orwell"},
        {"title": "Shoe Dog", "author": "Phil Knight"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "One Flew Over the Cuckoo's Nest", "author": "Ken Kesey"},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
    ]
    first_three = books[:3]
    return books, first_three

def student_database():
    students = {
        "Alice": "ID001",
        "Bob": "ID002",
        "Charlie": "ID003",
        "Diana": "ID004"
    }
    return students

def main():
    books, first_three = favorite_books()
    print("All favorite books:", books)
    print("First three books:", first_three)
    students = student_database()
    print("Student database:", students)

if __name__ == "__main__":
    main()
