# Library Management System

A simple Python-based library management system that allows users to manage book inventory with basic CRUD operations.

## Features

- **Add Books**: Add new books with title and author information
- **Search Books**: Search for books by title or author (case-insensitive)
- **Display Inventory**: View all books in the library
- **Persistent Storage**: Data is stored in JSON format for persistence
- **Sample Data**: Pre-loaded with 5 classic books for testing

## Project Structure

```
library_management/
├── data/
│   └── books.json          # JSON file storing book data
├── src/
│   └── library.py          # Main application logic
├── .gitignore             # Git ignore rules
├── main.py                # Alternative entry point
├── readme.md              # Project documentation
└── requirement.txt        # Python dependencies
```

## Prerequisites

- Python 3.6 or higher
- Virtual environment (recommended)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd library_management
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies** (if any)
   ```bash
   pip install -r requirement.txt
   ```

## How to Run

### Method 1: Direct execution
```bash
python src/library.py
```

### Method 2: Through main entry point
```bash
python main.py
```

## Usage

When you run the application, you'll see a menu with 4 options:

```
========================================
    LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. Search Book
3. Display Inventory
4. Exit
----------------------------------------
```

### Menu Options:

1. **Add Book**: Enter book title and author to add to inventory
2. **Search Book**: Search by partial title or author name
3. **Display Inventory**: View all books in the format:
   ```
   Inventory:
   - Book: Title - Author
   - Book: Title - Author
   ```
4. **Exit**: Close the application

## Sample Data

The application comes with 5 pre-loaded books:
- To Kill a Mockingbird - Harper Lee
- 1984 - George Orwell
- Pride and Prejudice - Jane Austen
- The Great Gatsby - F. Scott Fitzgerald
- Harry Potter and the Philosopher's Stone - J.K. Rowling

## Data Storage

- Books are stored in `data/books.json`
- Data persists between program runs
- JSON format allows easy backup and sharing
- If JSON file is missing, application starts with empty library

## Code Structure

### Main Functions:

- `load_books()`: Load books from JSON file
- `save_books()`: Save books to JSON file
- `add_book()`: Add new book to inventory
- `search_book()`: Search for books by title/author
- `display_inventory()`: Show all books
- `main()`: Main program loop with menu

## Assignment Requirements Met

✅ **Modular Design**: Each functionality in separate functions  
✅ **Add Books**: Function to add books to inventory  
✅ **Search Books**: Function to search by title/author  
✅ **Display Inventory**: Function to show all books  
✅ **Main Program**: Menu-driven interface calling all functions  

## Error Handling

- Input validation for empty fields
- Graceful handling of missing JSON file
- Safe file operations with try/except blocks

## Future Enhancements

- Book categories/genres
- Book availability status
- Due date tracking
- User management
- Database integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
