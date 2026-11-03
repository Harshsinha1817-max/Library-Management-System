# Library Management System

**PS No.:** 99 | **Programme:** Bachelor of Computer Application | **School of Information Technology, Rungta International Skills University**

## Project Overview
A console application, written in Python 3, that manages a library's books. A librarian can add books, issue them to members, take them back, search the catalogue by title or author, and view every book. All data is stored in a text file (`library.txt`), loaded when the program starts and saved when it exits.

## Objectives
- Apply Python lists, dictionaries, functions and file handling in one small project.
- Keep each feature in its own function so the code is easy to read, test and extend.
- Make sure a book that is already issued cannot be issued again.

## Features
| Menu option | Feature | Description |
|---|---|---|
| 1 | Add book | Asks for title and author, generates the next ID (first is `B101`) and marks the book Available |
| 2 | Issue book | Asks for Book ID and Member name; refuses unknown IDs and books that are already issued |
| 3 | Return book | Asks for Book ID and marks the book Available again |
| 4 | Search book | Search by title or author (partial, case-insensitive match) |
| 5 | Display all books | Lists every book with its status |
| 6 | Exit | Saves all data to `library.txt` and quits |

## Requirements
- Python 3.6 or later (no external libraries needed)

## Project Files
| File | Purpose |
|---|---|
| `one.py` | Complete program (single Python file) |
| `library.txt` | Data file (created or updated automatically) |
| `README.md` | This documentation |
| `test_cases.pdf` | Input and output of all four test cases |

## How to Run
```
python3 one.py
```
Optional: pass a different data file, e.g. `python3 one.py mydata.txt`.

## Data Design
Each book is a **dictionary** stored inside a **list**:
```python
{"id": "B101", "title": "Python Basics", "author": "Mark Lutz", "status": "Available", "member": ""}
```
File format (`library.txt`), one book per line:
```
B101|Python Basics|Mark Lutz|Available|
B102|Data Science|Wes McKinney|Issued|Riya
```

## Test Cases
| # | Scenario | Input | Expected output |
|---|---|---|---|
| 1 | Normal input | Option 1, Title: `Python Basics`, Author: `Mark Lutz` | `Book added. ID: B101 \| Python Basics \| Mark Lutz \| Available` |
| 2 | Boundary (only book B101) | Option 2, ID: `B101`, Member: `Riya` | `Book B101 issued to Riya. Status: Issued` and `Available books: 0` |
| 3 | Invalid input | Option 2, ID: `B999` | `Book ID B999 not found.` |
| 4 | Different valid scenario | (a) Option 1: `Data Science`, `Wes McKinney`; (b) Option 4 by author: `McKinney`; (c) Option 3: `B101` | (a) `Book added. ID: B102 \| Data Science \| Wes McKinney \| Available`; (b) `B102 \| Data Science \| Wes McKinney \| Available`; (c) `Book B101 returned. Status: Available` |

Test cases 2 to 4 start with B101 already in `library.txt`; for test 4, B101 is in the Issued state (as left by test 2).

## Sample Session
```
===== Library Management System =====
1. Add book
2. Issue book
3. Return book
4. Search book
5. Display all books
6. Exit
Enter choice: 1
Title: Python Basics
Author: Mark Lutz
Book added. ID: B101 | Python Basics | Mark Lutz | Available
```

## Error Handling
- Unknown Book ID: `Book ID <id> not found.`
- Issuing an already issued book: refused with a message.
- Returning a book that is not issued: refused with a message.
- Invalid menu choice or search option: asks the user to try again.
- Missing data file: the program starts with an empty library.
