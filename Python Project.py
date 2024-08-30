def welcome_message():
    print("Welcome to the Expense Tracker!")
    print("Track your daily expenses and manage your budget effectively.\n")

def log_expense(expenses):
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
            if amount <= 0:
                print("Amount should be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")
    
    categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"]
    print("\nExpense Categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            category_choice = int(input("\nSelect the expense category (choose the number): "))
            if 1 <= category_choice <= len(categories):
                category = categories[category_choice - 1]
                break
            else:
                print(f"Please select a valid category number between 1 and {len(categories)}.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to a category.")
    
    description = input("Enter a description for the expense: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    print("\nExpense logged successfully!\n")

def display_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal amount spent: £{total_spent:.2f}")

    category_totals = {}
    for expense in expenses:
        category = expense['category']
        category_totals[category] = category_totals.get(category, 0) + expense['amount']

    print("\nAmount spent by category:")
    for category, total in category_totals.items():
        print(f"{category}: £{total:.2f}")

    print("\nAll recorded expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['description']} - £{expense['amount']:.2f} ({expense['category']})")
    print()

def thank_you_message():
    print("Thank you for using the Expense Tracker!")

def run_expense_tracker():
    expenses = []
    
    welcome_message()
    
    while True:
        print("Options:")
        print("1. Log a new expense")
        print("2. View summary of expenses")
        print("3. Exit")

        choice = input("Please select an option (1/2/3): ")

        if choice == "1":
            log_expense(expenses)
        elif choice == "2":
            display_summary(expenses)
        elif choice == "3":
            thank_you_message()
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    run_expense_tracker()
