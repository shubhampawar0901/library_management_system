# Simple library management system
# Global list to store all books

import json
import os

DATA_FILE = "data/books.json"

# books = []

def load_books():
    """load books from json file"""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except:
        return []

def add_book():
    """Add a new book to the library inventory."""
    print("\n--- Add New Book ---")
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    
    if title and author:
        books = load_books()
        book = {"title": title, "author": author}
        books.append(book)
        with open(DATA_FILE, 'w') as file:
            json.dump(books, file, indent=4)
        print(f"Book '{title}' by {author} added successfully!")
    else:
        print("Error: Both title and author are required!")

def search_book():
    """Search for a book by title or author."""
    print("\n--- Search Book ---")
    search_term = input("Enter title or author to search: ").strip().lower()
    
    if not search_term:
        print("Error: Please enter a search term!")
        return
    
    found_books = []
    books = load_books()
    for book in books:
        if search_term in book["title"].lower() or search_term in book["author"].lower():
            found_books.append(book)
    
    if found_books:
        print(f"\nFound {len(found_books)} book(s):")
        for book in found_books:
            print(f"- Book: {book['title']} - {book['author']}")
    else:
        print("No books found matching your search.")

def display_inventory():
    """Display all books in the library inventory."""
    print("\n--- Library Inventory ---")
    
    books = load_books()
    if not books:
        print("No books in the library yet.")
        return
    
    print("Inventory:")
    for book in books:
        print(f"- Book: {book['title']} - {book['author']}")

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Book")
    print("2. Search Book")
    print("3. Display Inventory")
    print("4. Exit")
    print("-"*40)

def main():
    """Main program loop."""
    print("Welcome to Library Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            print("\nThank you for using Library Management System!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()