import json 
import os
from datetime import date, datetime


DATA_FILE = 'expenses.json'

def load_expenses(): 
    if not os.path.exists(DATA_FILE): 
        return []

    with open(DATA_FILE, 'r') as f: 
        try: 
            data = json.load(f)
            if not isinstance(data, list): 
                return []
            return data
        except json.JSONDecodeError:
            return[]
        

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f: 
        json.dump(expenses, f, indent=2)


def input_float(prompt): 
    while True: 
        raw = input(prompt).strip() 
        try: 
            value = float(raw)
            return value 
        except ValueError: 
            print("Please enter a valid number (e.g., 12.34).")

def input_date(prompt): 
    while True: 
        raw = input(prompt).strip() 
        try: 
            dt = datetime.strptime(raw, "%Y-%m-%d").date()
            return dt.isoformat()
        except ValueError: 
            print("Please enter a valid date in YYYY-MM-DD format.") 


def add_expense(expenses): 
    print('\n--- Add Expense ---') 
    
    amount = input_float("Amount: ")
    category = input("Category (e.g., Food, Transport): ").strip()
    if category == "": 
        category = "uncategorized"
    
    description = input("Description: ").strip()
    expense_date = input_date("Date: ")

    expense = {
        "amount" : amount,
        "category" : category,
        "description" : description,
        "date" : expense_date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")
def main(): 

    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Summary by category")
        print("4. Summary by month")
        print("5. Delete an expense")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            summary_by_category(expenses)
        elif choice == "4":
            summary_by_month(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "0":
            print("Goodbye!")
            save_expenses(expenses)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()