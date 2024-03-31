from expense import Expense
import calendar
import datetime


def main():
    print(f"🎯 Running Expense Tracker ")
    expense_file_path = "expenses.csv"
    budget = 4000

    # Get user input for expense 
    expense = get_user_expense()
    #Write their expense to a file 
    save_expense_file(expense, expense_file_path )
    #Read the file and summarize the expenses
    summarize_the_file(expense_file_path, budget)


    


def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_catagory= expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_catagory, amount=expense_amount)
            return new_expense
        else:
            print(f"Invalid category. Please enter a number {value_range}")

def save_expense_file(expense, expense_file_path):
    print(f"🎯 Saving Expense : {expense} to {expense_file_path}")
    with open(expense_file_path, 'a' , encoding='utf-8') as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

expenses: list[Expense] = []  # Define the "expenses" list

def summarize_the_file(expense_file_path, budget):
    print(f"🎯 Summarizing the file")
    with open(expense_file_path, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) < 3:
                print(f"Skipping line: {line}")
                continue
            expense_name, expense_category, expense_amount = parts
            print(f" {expense_name} spent {expense_amount} on {expense_category}")
            line_expense = Expense(name=str(expense_name), category=str(expense_category), amount=float(expense_amount))
            print(line_expense)
            expenses.append(line_expense)  # Append to the "expenses" list
    print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses By Category 📈")
    for key, amount in amount_by_category.items():
        print(f"Total expense for {key} is ₹{amount:.2f}")

    total_spent = sum([expense.amount for expense in expenses])
    print(f"Total spent: ₹{total_spent:.2f} this month!")

    Remaining_budget = budget - total_spent
    print(f"Total left: ₹{Remaining_budget:.2f} this month!")

    now = datetime.datetime.now()

    days_in_month = calendar.monthrange(now.year, now.month)[1]

    remaining_days = days_in_month - now.day

    print("remaining days in month: ", remaining_days)
    if remaining_days == 0:
        print(green("No remaining days in this month."))
    else:
        daily_budget = Remaining_budget / remaining_days
        print(green(f"Daily budget: ₹{daily_budget:.2f}"))


def green(text):
    return f"\033[92m{text}\033[0m"

    
    

        
if __name__ == "__main__":
    main()

