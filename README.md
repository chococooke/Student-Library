# Central Library System

## Overview
The Central Library System is a simple Python project designed to simulate the operations of a library. It allows users to list available books, issue books, and return books. This project is a great way to practice object-oriented programming and basic Python input/output operations.

## Features
- List all available books
- Issue a book
- Return a book

## Classes

### CentralLibrary
This class represents the library and manages the book inventory.

**Methods:**
- `__init__(self, bookList)`: Initializes the library with a list of books.
- `listAllBooks(self)`: Lists all available books in the library.
- `issueBook(self, bookName)`: Issues a book to a user if it's available.
- `returnBook(self, bookName)`: Returns a book to the library.

### Student
This class simulates the actions a student can perform in the library.

**Methods:**
- `issueBook()`: Prompts the user to enter the name of the book they want to issue.
- `returnBook()`: Prompts the user to enter the name of the book they want to return.

## Usage
To use this system, run the script. You will be presented with a welcome message and options to perform various actions in the library.

```plaintext
[=== Welcome to Central Library ===]
Options:
    1. List available books
    2. Issue A book
    3. Return A book
    -----------------
    Press 'q' to quit.
[==================================]
```

### Options:
- **1**: List all available books.
- **2**: Issue a book by entering the book's name.
- **3**: Return a book by entering the book's name.
- **q**: Quit the system.

## Example
```plaintext
[=== Welcome to Central Library ===]
Options:
    1. List available books
    2. Issue A book
    3. Return A book
    -----------------
    Press 'q' to quit.
[==================================]

Enter your choice : 1
1. Harry Potter
2. LOTR
3. Linux Fundamentals
4. Desi Boyz

Enter your choice : 2
Enter the book you want to issue : Harry Potter
The book Harry Potter has been successfully issued to you.
Keep it safe and consider returning it within 30 days.
Thank you!

Enter your choice : q
Thank you for using Central Library. Visit again!
```

## Requirements
- Python 3.x

## How to Run
1. Save the code in a file, for example, `central_library.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the script using the command: `python central_library.py`.

Enjoy using the Central Library System!
