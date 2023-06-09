import json
from datetime import datetime, timedelta


def form_balance_sheet(input_data):
    expense_data = input_data.get("expenseData", [])
    revenue_data = input_data.get("revenueData", [])

    balance_sheet = []
    
    # Create a dictionary to store the monthly revenue and expense totals
    monthly_totals = {}
    
    # Iterate over the expense data
    for expense in expense_data:
        amount = expense.get("amount", 0)
        start_date = expense.get("startDate")
        month_year = start_date[:7]  # Extract the year and month
        
        # Subtract the expense amount from the monthly total
        if month_year in monthly_totals:
            monthly_totals[month_year] -= amount
        else:
            monthly_totals[month_year] = -amount
    
    # Iterate over the revenue data
    for revenue in revenue_data:
        amount = revenue.get("amount", 0)
        start_date = revenue.get("startDate")
        month_year = start_date[:7]  # Extract the year and month
        
        # Add the revenue amount to the monthly total
        if month_year in monthly_totals:
            monthly_totals[month_year] += amount
        else:
            monthly_totals[month_year] = amount
    
    # Determine the start and end dates for the balance sheet
    start_date = min(monthly_totals.keys())
    end_date = max(monthly_totals.keys())
    
    # Generate the balance sheet entries for each month
    current_date = datetime.strptime(start_date, "%Y-%m")
    end_date = datetime.strptime(end_date, "%Y-%m")
    while current_date <= end_date:
        month_year = current_date.strftime("%Y-%m")
        balance = monthly_totals.get(month_year, 0)
        next_month = current_date.replace(day=28) + timedelta(days=4)  # Get the next month
        last_day_of_month = next_month - timedelta(days=next_month.day)
        balance_sheet.append({"amount": balance, "startDate": month_year + "-01T00:00:00.000Z"})
        current_date = last_day_of_month + timedelta(days=1)
    
    return balance_sheet

# Read the input JSON file
with open('2-input.json', 'r') as input_file:
    input_data = json.load(input_file)

# Calculate the balance sheet
balance_sheet = form_balance_sheet(input_data)

# Convert the output to JSON format
output_json = json.dumps({"balance": balance_sheet}, indent=2)

print(output_json)

