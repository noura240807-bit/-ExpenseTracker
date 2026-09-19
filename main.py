import json
import os

FILENAME = "expenses.json"

# Load existing expenses (file irundha)
def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

# Expenses ah file la save pannradhu
def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)

# Pudhu expense add pannradhu
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (food, travel, etc.): ")
    date = input("Enter date (dd-mm-yyyy): ")
    expenses.append({"amount": amount, "category": category, "date": date})
    save_expenses(expenses)
    print("Expense added!\n")

# Ella expenses um list pannradhu
def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.\n")
        return
    print("\n--- All Expenses ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} | {e['category']} | Rs.{e['amount']}")
    print()

# Total expense calculate pannradhu
def total_expense(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"Total spent: Rs.{total}\n")

# Main menu loop
def main():
    expenses = load_expenses()

    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            print("Tata Bye Bye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()