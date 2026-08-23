import json
import os
from datetime import datetime, timedelta

DATA_FILE = "library_data.json"
LOAN_DAYS = 14
FINE_PER_DAY = 5

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def get_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must be at most {maximum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_float(prompt, minimum=None):
    while True:
        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def generate_id(items, prefix):
    if not items:
        return f"{prefix}001"

    numbers = []

    for item in items:
        item_id = item.get("id", "")

        try:
            number = int(item_id.replace(prefix, ""))
            numbers.append(number)
        except ValueError:
            pass

    next_number = max(numbers, default=0) + 1

    return f"{prefix}{next_number:03d}"

    class DataManager:

    def __init__(self, filename):
        self.filename = filename

    def default_data(self):
        return {
            "books": [],
            "members": [],
            "loans": [],
            "transactions": []
        }

    def load_data(self):
        if not os.path.exists(self.filename):
            return self.default_data()

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            # Make sure required keys exist
            default = self.default_data()

            for key in default:
                if key not in data:
                    data[key] = default[key]

            return data

        except json.JSONDecodeError:
            print("Warning: Data file is corrupted.")
            print("Starting with empty database.")

            return self.default_data()

    def save_data(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("\nData saved successfully.")

class Book:

    def __init__(
        self,
        book_id,
        title,
        author,
        category,
        year,
        quantity
    ):
        self.id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.year = year
        self.quantity = quantity
        self.available = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "year": self.year,
            "quantity": self.quantity,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["id"],
            data["title"],
            data["author"],
            data["category"],
            data["year"],
            data["quantity"]
        )

        book.available = data.get(
            "available",
            data["quantity"]
        )

        return book

class Member:

    def __init__(
        self,
        member_id,
        name,
        phone,
        email,
        address
    ):
        self.id = member_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["phone"],
            data["email"],
            data["address"]
        )

class Loan:

    def __init__(
        self,
        loan_id,
        book_id,
        member_id,
        borrow_date,
        due_date,
        return_date=None,
        fine=0
    ):
        self.id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date
        self.fine = fine

    def to_dict(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "member_id": self.member_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "return_date": self.return_date,
            "fine": self.fine
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["book_id"],
            data["member_id"],
            data["borrow_date"],
            data["due_date"],
            data.get("return_date"),
            data.get("fine", 0)
        )