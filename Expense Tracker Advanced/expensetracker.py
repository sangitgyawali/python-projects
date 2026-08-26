expenses = []

def add_expense():
    name = input("What did you buy? ")
    amount = float(input("How much did it costs?"))
    category = input("Category:")

    expense = {
        "name" = name
        "amount" = amount
        "catgory" = category
    }

    expenses.append(expenses)

    print("Expense added successfully!")

def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")

    for expense in expenses:
        print(
            f"{expense['name']} | "
            f"Rs. {expense['amount']} | "
            f"{expense['category']}"
        )
        )

def show_total():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]

    print(f"Total spending: Rs. {total}")
