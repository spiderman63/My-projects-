import mysql.connector
import datetime

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(
                                   
        host="localhost",     # Your MySQL server host
        user="root",          # MySQL username
        password="Aa@1111111111",  # MySQL password
        database="finance_tracker"
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)  # Exit if connection fails

# Variables to track total income, expenses, and remaining balance
total_income = 0.0
total_expenses = 0.0
remaining_balance = 0.0

# Function to initialize totals from existing transactions
def initialize_totals():
    global total_income, total_expenses, remaining_balance

    cursor.execute("SELECT SUM(amount) FROM ledger WHERE type='Income';")
    total_income_row = cursor.fetchone()
    total_income = total_income_row[0] if total_income_row[0] is not None else 0.0

    cursor.execute("SELECT SUM(amount) FROM ledger WHERE type='Expense';")
    total_expenses_row = cursor.fetchone()
    total_expenses = total_expenses_row[0] if total_expenses_row[0] is not None else 0.0

    remaining_balance = total_income - total_expenses

# Function to add a transaction (income or expense)
def add_transaction(transaction_type, amount, category):
    global total_income, total_expenses, remaining_balance

    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time

    cursor.execute('''
        INSERT INTO ledger (type, amount, category, date)
        VALUES (%s, %s, %s, %s)
    ''', (transaction_type, amount, category, date))

    conn.commit()  # Save the changes to the database

    # Update totals based on transaction type
    if transaction_type == 'Income':
        total_income += amount
    elif transaction_type == 'Expense':
        total_expenses += amount

    # Recalculate remaining balance
    remaining_balance = total_income - total_expenses

    print(f"{transaction_type} of {amount} in category '{category}' added.")
    print(f"Remaining balance: {remaining_balance:.2f}")

# Function to view all transactions
def view_transactions():
    cursor.execute('SELECT * FROM ledger')  # Fetch all data from the ledger table
    transactions = cursor.fetchall()

    if transactions:
        for transaction in transactions:
            print(f"ID: {transaction[0]} | Type: {transaction[1]} | Amount: {transaction[2]} | Category: {transaction[3]} | Date: {transaction[4]}")
    else:
        print("No transactions found.")

# Function to view total income and expenses by category
def view_summary():
    cursor.execute('''
        SELECT category, SUM(amount) FROM ledger GROUP BY category
    ''')
    
    summary = cursor.fetchall()
    
    if summary:
        for category, total in summary:
            print(f"Category: {category} | Total: {total}")
    else:
        print("No transactions found to summarize.")

# Function to display total income, total expenses, and remaining balance
def view_totals():
    print(f"Total Income: {total_income:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")
    print(f"Remaining Balance: {remaining_balance:.2f}")

# Simple menu for the user to choose options
def menu():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary by Category")
        print("5. View Totals (Income, Expenses, Balance)")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter income amount: "))
                category = input("Enter category (e.g., Salary, Business): ")
                add_transaction('Income', amount, category)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif choice == '2':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter category (e.g., Food, Bills, Entertainment): ")
                add_transaction('Expense', amount, category)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif choice == '3':
            view_transactions()

        elif choice == '4':
            view_summary()

        elif choice == '5':
            view_totals()  # Show totals in the menu

        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option, please try again.")

# Initialize totals from existing transactions
initialize_totals()

# Run the program
menu()

# Close the connection to the database
if conn.is_connected():
    cursor.close()
    conn.close()