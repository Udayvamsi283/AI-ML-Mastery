class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Issued: {book}")
        else:
            print(f"{book} is not available in the library.")
    
    def return_book(self, book):
        self.books.append(book)
        print(f"Returned: {book}")

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)

# Example usage:
if __name__ == "__main__":
    library = Library()
    library.add_book("The Great Gatsby")
    library.add_book("To Kill a Mockingbird")
    library.add_book("1984")
    
    library.display_books()
    
    library.issue_book("1984")
    library.display_books()
    
    library.return_book("1984")
    library.display_books()