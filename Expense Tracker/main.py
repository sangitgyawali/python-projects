expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append({"name": name, "amount": amount})
    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== EXPENSE LIST =====")
    total = 0

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - {expense['amount']}")
        total += expense["amount"]

    print("------------------------")
    print(f"Total Expense: {total}")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        index = int(input("Enter expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            expenses.pop(index)
            print("Expense deleted successfully.")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        print("Thank you for using Expense Tracker.")
        break
    else:
        print("Invalid choice. Please try again.")