import json
from datetime import datetime, timedelta

FILE = "library.json"
FINE_PER_DAY = 5
LOAN_DAYS = 14


class Library:

    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []
        self.load()

    def load(self):
        try:
            with open(FILE, "r") as f:
                data = json.load(f)
                self.books = data["books"]
                self.members = data["members"]
                self.loans = data["loans"]
        except:
            self.books = []
            self.members = []
            self.loans = []

    def save(self):
        data = {
            "books": self.books,
            "members": self.members,
            "loans": self.loans
        }

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

    def find_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member["id"] == member_id:
                return member
        return None

    def add_book(self):
        print("\n--- ADD BOOK ---")

        book = {
            "id": input("Book ID: "),
            "title": input("Title: "),
            "author": input("Author: "),
            "year": input("Year: "),
            "quantity": int(input("Quantity: "))
        }

        self.books.append(book)
        self.save()

        print("Book added successfully.")

    def show_books(self):
        print("\n--- BOOKS ---")

        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            print(
                f"{book['id']} | "
                f"{book['title']} | "
                f"{book['author']} | "
                f"{book['year']} | "
                f"Qty: {book['quantity']}"
            )

    def search_book(self):
        keyword = input(
            "\nEnter title or author: "
        ).lower()

        found = False

        for book in self.books:
            if (
                keyword in book["title"].lower()
                or keyword in book["author"].lower()
            ):
                print(
                    f"{book['id']} | "
                    f"{book['title']} | "
                    f"{book['author']}"
                )
                found = True

        if not found:
            print("Book not found.")

    def delete_book(self):
        book_id = input("\nBook ID: ")

        book = self.find_book(book_id)

        if book:
            self.books.remove(book)
            self.save()
            print("Book deleted.")
        else:
            print("Book not found.")

    def add_member(self):
        print("\n--- ADD MEMBER ---")

        member = {
            "id": input("Member ID: "),
            "name": input("Name: "),
            "phone": input("Phone: "),
            "email": input("Email: ")
        }

        self.members.append(member)
        self.save()

        print("Member added.")

    def show_members(self):
        print("\n--- MEMBERS ---")

        if not self.members:
            print("No members.")
            return

        for member in self.members:
            print(
                f"{member['id']} | "
                f"{member['name']} | "
                f"{member['phone']} | "
                f"{member['email']}"
            )

    def delete_member(self):
        member_id = input("\nMember ID: ")

        member = self.find_member(member_id)

        if member:
            self.members.remove(member)
            self.save()
            print("Member deleted.")
        else:
            print("Member not found.")

    def borrow_book(self):
        print("\n--- BORROW BOOK ---")

        book_id = input("Book ID: ")
        member_id = input("Member ID: ")

        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not book:
            print("Book not found.")
            return

        if not member:
            print("Member not found.")
            return

        if book["quantity"] <= 0:
            print("Book is not available.")
            return

        for loan in self.loans:
            if (
                loan["book_id"] == book_id
                and loan["member_id"] == member_id
                and not loan["returned"]
            ):
                print("Member already has this book.")
                return

        borrow_date = datetime.now()
        due_date = (
            borrow_date +
            timedelta(days=LOAN_DAYS)
        )

        loan = {
            "book_id": book_id,
            "member_id": member_id,
            "borrow_date": borrow_date.strftime(
                "%Y-%m-%d"
            ),
            "due_date": due_date.strftime(
                "%Y-%m-%d"
            ),
            "returned": False
        }

        self.loans.append(loan)
        book["quantity"] -= 1

        self.save()

        print("Book borrowed successfully.")
        print("Due date:", loan["due_date"])

    def return_book(self):
        print("\n--- RETURN BOOK ---")

        book_id = input("Book ID: ")
        member_id = input("Member ID: ")

        loan = None

        for item in self.loans:
            if (
                item["book_id"] == book_id
                and item["member_id"] == member_id
                and not item["returned"]
            ):
                loan = item
                break

        if not loan:
            print("Borrow record not found.")
            return

        book = self.find_book(book_id)

        if book:
            book["quantity"] += 1

        today = datetime.now().date()

        due = datetime.strptime(
            loan["due_date"],
            "%Y-%m-%d"
        ).date()

        late_days = (today - due).days

        if late_days > 0:
            fine = late_days * FINE_PER_DAY
            print(f"Late by {late_days} days.")
            print(f"Fine: Rs. {fine}")
        else:
            print("Returned on time.")
            print("Fine: Rs. 0")

        loan["returned"] = True

        self.save()

        print("Book returned successfully.")

    def show_loans(self):
        print("\n--- BORROWED BOOKS ---")

        found = False

        for loan in self.loans:

            if not loan["returned"]:

                book = self.find_book(
                    loan["book_id"]
                )

                member = self.find_member(
                    loan["member_id"]
                )

                print(
                    f"Book: {book['title']}"
                )

                print(
                    f"Member: {member['name']}"
                )

                print(
                    f"Borrowed: "
                    f"{loan['borrow_date']}"
                )

                print(
                    f"Due: "
                    f"{loan['due_date']}"
                )

                print("-" * 40)

                found = True

        if not found:
            print("No books are currently borrowed.")

    def statistics(self):
        total_books = len(self.books)

        total_copies = sum(
            book["quantity"]
            for book in self.books
        )

        total_members = len(self.members)

        borrowed = sum(
            1
            for loan in self.loans
            if not loan["returned"]
        )

        returned = sum(
            1
            for loan in self.loans
            if loan["returned"]
        )

        print("\n--- STATISTICS ---")

        print("Different books:", total_books)
        print("Available copies:", total_copies)
        print("Members:", total_members)
        print("Currently borrowed:", borrowed)
        print("Returned books:", returned)

    def book_menu(self):
        while True:

            print("""
--- BOOK MENU ---

1. Add Book
2. Show Books
3. Search Book
4. Delete Book
5. Back
""")

            choice = input("Choice: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.show_books()

            elif choice == "3":
                self.search_book()

            elif choice == "4":
                self.delete_book()

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

    def member_menu(self):
        while True:

            print("""
--- MEMBER MENU ---

1. Add Member
2. Show Members
3. Delete Member
4. Back
""")

            choice = input("Choice: ")

            if choice == "1":
                self.add_member()

            elif choice == "2":
                self.show_members()

            elif choice == "3":
                self.delete_member()

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

    def loan_menu(self):
        while True:

            print("""
--- LOAN MENU ---

1. Borrow Book
2. Return Book
3. Show Borrowed Books
4. Back
""")

            choice = input("Choice: ")

            if choice == "1":
                self.borrow_book()

            elif choice == "2":
                self.return_book()

            elif choice == "3":
                self.show_loans()

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

    def run(self):
        while True:

            print("""
==============================
   LIBRARY MANAGEMENT SYSTEM
==============================

1. Book Management
2. Member Management
3. Loan Management
4. Statistics
5. Exit
""")

            choice = input("Choice: ")

            if choice == "1":
                self.book_menu()

            elif choice == "2":
                self.member_menu()

            elif choice == "3":
                self.loan_menu()

            elif choice == "4":
                self.statistics()

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")


library = Library()
library.run()