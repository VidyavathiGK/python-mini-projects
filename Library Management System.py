import datetime

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {'Yes' if self.is_available else 'No'}"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"ID: {self.member_id}, Name: {self.name}, Books Borrowed: {len(self.borrowed_books)}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.book_id_counter = 1
        self.member_id_counter = 1

    def add_book(self, title, author):
        book = Book(title, author, self.book_id_counter)
        self.books.append(book)
        self.book_id_counter += 1
        print(f"Book '{title}' added successfully.")

    def add_member(self, name):
        member = Member(name, self.member_id_counter)
        self.members.append(member)
        self.member_id_counter += 1
        print(f"Member '{name}' added successfully.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def issue_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book:
            print("Error: Book not found.")
            return
        if not member:
            print("Error: Member not found.")
            return

        if book.is_available:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"Book '{book.title}' issued to {member.name}.")
        else:
            print("Error: Book is not available.")

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book:
            print("Error: Book not found.")
            return
        if not member:
            print("Error: Member not found.")
            return

        if book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned by {member.name}.")
        else:
            print("Error: This member did not borrow this book.")

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if not available_books:
            print("No books are currently available.")
        else:
            print("\n--- Available Books ---")
            for book in available_books:
                print(book)

    def display_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            print("\n--- Library Members ---")
            for member in self.members:
                print(member)

def main():
    library = Library()
    
    # Pre-populate with some data
    library.add_book("The Hobbit", "J.R.R. Tolkien")
    library.add_book("1984", "George Orwell")
    library.add_member("Alice")
    library.add_member("Bob")

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display Available Books")
        print("6. Display Members")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            name = input("Enter member name: ")
            library.add_member(name)
        elif choice == '3':
            book_id = int(input("Enter book ID to issue: "))
            member_id = int(input("Enter member ID: "))
            library.issue_book(book_id, member_id)
        elif choice == '4':
            book_id = int(input("Enter book ID to return: "))
            member_id = int(input("Enter member ID: "))
            library.return_book(book_id, member_id)
        elif choice == '5':
            library.display_available_books()
        elif choice == '6':
            library.display_members()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
