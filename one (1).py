"""
Library Management System (PS No. 99)
Console application to manage a library's books.

Concepts used: Lists, Dictionaries, Functions, File Handling
Data file   : library.txt  (one book per line: id|title|author|status|member)
"""

import os
import sys

DATA_FILE = "library.txt"
FIRST_ID_NUMBER = 101  # first generated ID is B101

AVAILABLE = "Available"
ISSUED = "Issued"


# ----------------------------------------------------------------------
# File handling
# ----------------------------------------------------------------------
def load_books(filename):
    """Load books from the file into a list of dictionaries."""
    books = []
    if not os.path.exists(filename):
        return books
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) < 4:
                continue  # skip malformed lines
            book = {
                "id": parts[0],
                "title": parts[1],
                "author": parts[2],
                "status": parts[3],
                "member": parts[4] if len(parts) > 4 else "",
            }
            books.append(book)
    return books


def save_books(books, filename):
    """Save the list of book dictionaries to the file."""
    with open(filename, "w", encoding="utf-8") as f:
        for b in books:
            f.write("{}|{}|{}|{}|{}\n".format(
                b["id"], b["title"], b["author"], b["status"], b["member"]))


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------
def generate_id(books):
    """Generate the next book ID (B101, B102, ...)."""
    highest = FIRST_ID_NUMBER - 1
    for b in books:
        digits = b["id"][1:]
        if digits.isdigit() and int(digits) > highest:
            highest = int(digits)
    return "B{}".format(highest + 1)


def find_book(books, book_id):
    """Return the book dictionary with the given ID, or None."""
    for b in books:
        if b["id"].upper() == book_id.upper():
            return b
    return None


def format_book(b):
    return "{} | {} | {} | {}".format(b["id"], b["title"], b["author"], b["status"])


def count_available(books):
    return sum(1 for b in books if b["status"] == AVAILABLE)


# ----------------------------------------------------------------------
# Features
# ----------------------------------------------------------------------
def add_book(books):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    if not title or not author:
        print("Title and author cannot be empty.")
        return
    book = {
        "id": generate_id(books),
        "title": title,
        "author": author,
        "status": AVAILABLE,
        "member": "",
    }
    books.append(book)
    print("Book added. ID: " + format_book(book))


def issue_book(books):
    book_id = input("Book ID: ").strip()
    book = find_book(books, book_id)
    if book is None:
        print("Book ID {} not found.".format(book_id))
        return
    if book["status"] == ISSUED:
        print("Book {} is already issued to {}.".format(book["id"], book["member"]))
        return
    member = input("Member: ").strip()
    if not member:
        print("Member name cannot be empty.")
        return
    book["status"] = ISSUED
    book["member"] = member
    print("Book {} issued to {}. Status: {}".format(book["id"], member, ISSUED))
    print("Available books: {}".format(count_available(books)))


def return_book(books):
    book_id = input("Book ID: ").strip()
    book = find_book(books, book_id)
    if book is None:
        print("Book ID {} not found.".format(book_id))
        return
    if book["status"] == AVAILABLE:
        print("Book {} is not issued.".format(book["id"]))
        return
    book["status"] = AVAILABLE
    book["member"] = ""
    print("Book {} returned. Status: {}".format(book["id"], AVAILABLE))


def search_books(books):
    choice = input("Search by (1) Title or (2) Author: ").strip()
    if choice == "1":
        field = "title"
    elif choice == "2":
        field = "author"
    else:
        print("Invalid search option.")
        return
    keyword = input("Enter {}: ".format(field)).strip().lower()
    results = [b for b in books if keyword and keyword in b[field].lower()]
    if not results:
        print("No books found.")
        return
    for b in results:
        print(format_book(b))


def display_all(books):
    if not books:
        print("No books in the library.")
        return
    for b in books:
        print(format_book(b))


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add book")
    print("2. Issue book")
    print("3. Return book")
    print("4. Search book")
    print("5. Display all books")
    print("6. Exit")


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else DATA_FILE
    books = load_books(filename)  # load data at start

    while True:
        show_menu()
        try:
            choice = input("Enter choice: ").strip()
        except EOFError:
            choice = "6"
            print()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            issue_book(books)
        elif choice == "3":
            return_book(books)
        elif choice == "4":
            search_books(books)
        elif choice == "5":
            display_all(books)
        elif choice == "6":
            save_books(books, filename)  # save data on exit
            print("Data saved to {}. Goodbye!".format(filename))
            break
        else:
            print("Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
