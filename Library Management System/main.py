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