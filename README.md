# 📚 Library Management System

A simple and beginner-friendly **Library Management System** built using **Python** and **JSON**.
This project allows users to add books, view available books, issue books, return books, and store library data permanently in a JSON file.

---

## 🚀 Features

* 📖 Add new books
* 📚 View all books
* 📤 Issue a book
* 📥 Return a book
* 💾 Save library data in JSON format
* 🔄 Automatically load previously saved data
* 🖥️ Simple command-line interface
* ❌ Handles invalid book numbers and input errors

---

## 🛠️ Technologies Used

| Technology                   | Purpose                   |
| ---------------------------- | ------------------------- |
| 🐍 Python                    | Main programming language |
| 📄 JSON                      | Data storage              |
| 💻 Terminal / Command Prompt | User Interface            |

---

## 📂 Project Structure

```text
LibraryManagementSystem/
│
├── library.py
├── library.json
└── README.md
```

### Files Description

* **`library.py`** – Main Python program
* **`library.json`** – Stores library books and their issue status
* **`README.md`** – Project documentation

> `library.json` is automatically created when the program saves data.

---

## ⚙️ Requirements

Before running the project, make sure **Python 3.x** is installed on your computer.

Check your Python version:

```bash
python --version
```

or:

```bash
py --version
```

No external Python libraries are required because the project uses Python's built-in `json` module.

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
https://github.com/dharmendra-developer/Labrory_Management_System.git
```

### 2. Open the Project Folder

```bash
cd LibraryManagementSystem
```

### 3. Run the Program

```bash
python library.py
```

For Windows, you can also use:

```bash
py library.py
```

---

## 🖥️ Application Menu

When the program starts, you will see:

```text
1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. Exit
Enter choice:
```

---

## 📖 Example

### Add a Book

```text
Enter choice: 1
Enter book title: Python Programming
Book added
```

### View Books

```text
Enter choice: 2

Library Books:
1. Python Programming - Available
```

### Issue a Book

```text
Enter choice: 3

Library Books:
1. Python Programming - Available

Enter book number to issue: 1
Book issued
```

### Return a Book

```text
Enter choice: 4

Library Books:
1. Python Programming - Issued

Enter book number to return: 1
Book returned
```

### Exit

```text
Enter choice: 5
Data saved. Exiting...
```

---

## 💾 Data Storage

The project uses a JSON file to store book information.

Example:

```json
[
    {
        "title": "Python Programming",
        "issued": false
    },
    {
        "title": "Data Structures",
        "issued": true
    }
]
```

The `issued` value represents the current status of the book:

* `false` → Available
* `true` → Issued

---

## 🧠 Concepts Used

This project is useful for learning basic Python programming concepts such as:

* Variables
* Lists
* Dictionaries
* Functions
* `if-elif-else`
* `while` loops
* `for` loops
* `try-except`
* File handling
* JSON serialization
* JSON deserialization
* User input
* Basic CRUD operations

---

## 🎯 Learning Objectives

By completing this project, you can understand:

1. How to create functions in Python
2. How to work with lists and dictionaries
3. How to read and write JSON files
4. How to build a menu-driven application
5. How to handle user input
6. How to manage persistent data
7. How to create a basic real-world Python project

---

## 🔮 Future Improvements

The project can be extended with the following features:

* 🔐 Admin Login System
* 🆔 Unique Book ID
* ✍️ Author Name
* 👨‍🎓 Student/User Management
* 📅 Issue Date
* 📅 Return Date
* 🔍 Search Book
* ✏️ Update Book
* 🗑️ Delete Book
* 📊 Library Statistics
* 🗄️ SQLite/MySQL Database
* 🖥️ Tkinter GUI
* 🌐 Flask Web Application
* 📱 Responsive Web Interface

---

## 👨‍💻 Author

**Dharmendra Singh**

### Skills Demonstrated

`Python` • `JSON` • `File Handling` • `OOP Concepts` • `Exception Handling` • `CRUD Operations`

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📜 License

This project is created for **educational and learning purposes**.
