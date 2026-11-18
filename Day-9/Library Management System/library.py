class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        super().display()
        print("File Size:", self.file_size, "MB")

b1 = Book("Python Programming", "John")
e1 = EBook("Java Programming", "James", 15)

print("Book Details:")
b1.display()

print("\nEBook Details:")
e1.display()
