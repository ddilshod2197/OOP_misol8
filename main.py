class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"✅ '{book.title}' kitobi qo‘shildi")
    
    def show_books(self):
        print("\n📚 Kutubxonadagi kitoblar:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.title} - {book.author}")

# Test
lib = Library()
lib.add_book(Book("Python OOP", "Mark Lutz"))
lib.add_book(Book("Clean Code", "Robert Martin"))
lib.show_books()
