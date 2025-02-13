import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os


def create_csv(filename, headers):
    """Create a CSV file with the specified headers if it doesn't exist."""
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        print(f"CSV file '{filename}' created successfully.")


def log_expense(filename):
    """Log a new expense into the CSV file."""
    print("\n--- Log Expense ---")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    date = input("Enter the date (YYYY-MM-DD): ")

    # Validate date format
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")
        return

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, date])
    print("Expense logged successfully!")


def analyze_expenses(filename):
    """Analyze and display the expenses from the CSV file."""
    print("\n--- Analyze Expenses ---")
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print("No data found. Please log some expenses first.")
        return

    # Ensure the "Expenses" column is treated as numeric
    df["Expenses"] = pd.to_numeric(df["Expenses"], errors='coerce')

    total_spent = df["Expenses"].sum()
    print(f"\nTotal Spending: ${total_spent:.2f}")

    category_breakdown = df.groupby("Category")["Expenses"].sum().sort_values(ascending=False)
    print("\nCategory-wise Breakdown:")
    print(category_breakdown)

    df['Date'] = pd.to_datetime(df['Date'])
    daily_spending = df.groupby(df['Date'].dt.date)["Expenses"].sum()
    print("\nDaily Spending Trends:")
    print(daily_spending)


def visualize_expenses(filename):
    """Visualize the expenses using bar and line charts."""
    print("\n--- Visualize Expenses ---")
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print("No data found. Please log some expenses first.")
        return

    # Category-wise spending
    category_breakdown = df.groupby("Category")["Expenses"].sum()
    category_breakdown.plot(kind='bar', title="Category-wise Spending", xlabel="Category", ylabel="Amount")
    plt.show()

    # Daily spending trends
    df['Date'] = pd.to_datetime(df['Date'])
    daily_spending = df.groupby(df['Date'].dt.date)["Expenses"].sum()
    daily_spending.plot(kind='line', title="Daily Spending Trends", xlabel="Date", ylabel="Amount")
    plt.xticks(rotation=45)
    plt.show()


def main_menu():
    """Display the main menu and handle user choices."""
    filename = "Expenses.csv"
    headers = ["Category", "Expenses", "Date"]
    
    create_csv(filename, headers)

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Log Expense")
        print("2. Analyze Expenses")
        print("3. Visualize Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            log_expense(filename)
        elif choice == "2":
            analyze_expenses(filename)
        elif choice == "3":
            visualize_expenses(filename)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main_menu()