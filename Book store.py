import json
import os

BOOKS_FILE = "books.json"

# Load books from a JSON file.
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save books to a JSON file
def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Add a new book to the bookstore.
def add_book(books):
    
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    genre = input("Enter genre: ")
    
    # Validate price and quantity input
    while True:
        try:
            price = float(input("Enter price: "))
            if price < 0:
                raise ValueError("Price must be a positive number.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                raise ValueError("Quantity must be a non-negative integer.")
            break
        except ValueError as e:
            print(e)

    # Check for duplicate ISBN
    if any(book["ISBN"] == isbn for book in books):
        print("Error: Book with this ISBN already exists!")
        return
    
    book = {
        "Title": title,
        "Author": author,
        "ISBN": isbn,
        "Genre": genre,
        "Price": price,
        "Quantity": quantity
    }
    
    books.append(book)
    save_books(books)
    print("Book added successfully!")

def view_books(books):
    # Display all books in the bookstore
    if not books:
        print("No books available.")
        return
    
    print("\n--- List of Books ---")
    for book in books:
        print(f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}, Genre: {book['Genre']}, Price: {book['Price']}, Quantity: {book['Quantity']}")

def search_book(books):
    # Search for a book by title or ISBN.
    query = input("Enter book title or ISBN to search: ")
    found_books = [book for book in books if book["Title"].lower() == query.lower() or book["ISBN"] == query]
    
    if found_books:
        print("\n--- Search Results ---")
        for book in found_books:
            print(f"Found: {book}")
    else:
        print("Book not found.")

def remove_book(books):
    # Remove a book by ISBN.
    isbn = input("Enter ISBN of the book to remove: ")
    for book in books:
        if book["ISBN"] == isbn:
            books.remove(book)
            save_books(books)
            print("Book removed successfully!")
            return
    print("Error: Book not found.")

def main():
    # Main function to run the Bookstore Management System.
    books = load_books()
    
    if __name__ == "__main__":
        while True:
            print("\nBookstore Management System")
            print("1. Add Book")
            print("2. View Books")
            print("3. Search Book")
            print("4. Remove Book")
            print("5. Exit")
            
            choice = input("Enter your choice: Number ")

            if choice == "1":
                add_book(books)
            elif choice == "2":
                view_books(books)
            elif choice == "3":
                search_book(books)
            elif choice == "4":
                remove_book(books)
            elif choice == "5":
                save_books(books)
                print("Exiting program. Data saved.")
                break
            else:
                print("Invalid choice. Please try again.")

main()
