# Logic and Approach:

# 1. Define a class Book:
#   - Attributes: title, author, and pages are defined as private attributes.
#   - Methods:
#       - Constructor: Initializes the attributes.
#       - Getter and Setter Methods: Use Python's property decorators to get and set the values of the attributes.
#       - Class Method: calculate_reading_time calculates the reading time based on an assumed reading speed.
#       - String Representation: __str__() method provides a readable string representation of the object.
# 
# 2. Create an instance of Book:
#       - Instance Creation: Demonstrates how to create an instance and use the getter and setter methods to access and modify the attributes.
# 
# 3. Implement a subclass Ebook:
#       - Inheritance: Ebook class inherits from Book and adds an additional attribute format.
#       - Override Method: Overrides the __str__() method to include the new attribute.

class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        self._pages = pages

    @classmethod
    def calculate_reading_time(cls, pages, reading_speed=250):
        return pages * 250 / reading_speed

    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, Pages: {self._pages}"

class Ebook(Book):
    def __init__(self, title, author, pages, book_format):
        super().__init__(title, author, pages)
        self._format = book_format

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, book_format):
        self._format = book_format

    def __str__(self):
        return super().__str__() + f", Format: {self._format}"

# Demonstrate the use of getter and setter methods
book = Book("Atomic Habits", "F. Scott Fitzgerald", 218)
print(book)
book.pages = 200
print(book.pages)

# Demonstrate the Ebook subclass
ebook = Ebook("1984", "George Orwell", 328, "PDF")
print(ebook)
