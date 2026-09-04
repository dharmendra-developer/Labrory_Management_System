import json
library = []

def add_book():
    title = input("Enter book title: ")
    library.append({"title": title, "issued": False})
    print("Book added")

def show_books():
    if not library:
        print("No books available")
    else:
        print("\nLibrary Books:")
        for i, book in enumerate(library):
            status = "Issued" if book["issued"] else "Available"
            print(f"{i+1}. {book['title']} - {status}")

def issue_book():
    show_books()
    try:
        index = int(input("Enter book number to issue: ")) - 1
        if 0 <= index < len(library):
            if not library[index]["issued"]:
                library[index]["issued"] = True
                print("Book issued")
            else:
                print("Book already issued")
        else:
            print("Invalid choice")
    except:
        print("Enter valid number")

def return_book():
    show_books()
    try:
        index = int(input("Enter book number to return: ")) - 1
        if 0 <= index < len(library):
            if library[index]["issued"]:
                library[index]["issued"] = False
                print("Book returned")
            else:
                print("Book was not issued")
        else:
            print("Invalid choice")
    except:
        print("Enter valid number")

def save_data():
    with open("library.json", "w") as file:
        json.dump(library, file)

def load_data():
    try:
        with open("library.json", "r") as file:
            data = json.load(file)
        library.extend(data)
    except:
        pass

# Load existing data
load_data()

# Menu loop
while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        save_data()
        print("Data saved. Exiting...")
        break
    else:
        print("Invalid choice")
