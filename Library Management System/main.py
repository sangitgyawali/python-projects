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