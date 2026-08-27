#PROGRAM 5: FINANCIAL PERFORMANCE & PROFIT/LOS ESTIMATOR

# Input Data
revenue_p3 = 9.23
cogs_p2_p7 = 150.00
expense_p1 = 25.00
payroll_p4 = 216.00
expenses_p1_p4 = expense_p1 + payroll_p4

# Calculation Function
def calculate_financials():
    gross_profit = revenue_p3 - cogs_p2_p7
    net_profit = gross_profit - expenses_p1_p4
    return gross_profit, net_profit

# Call Calculation
gross_profit, net_profit = calculate_financials()

# Display Output
print("Prog 5: Financial Performance & Profit/Loss Estimator ")
print("=" * 40)
print("FINANCIAL PERFORMANCE SUMMARY")
print("=" * 40)
print("Revenue (Prog 3): $", revenue_p3)
print("COGS (Prog 2 + 7): -$", cogs_p2_p7)
print("-" *40)
print("Gross Profit: $", round(gross_profit, 2))
print("Expenses (Prog 1 + 4): -$", expenses_p1_p4)
print("-" * 40)
print("NET PROFIT/LOSS: $", round(net_profit, 2))
print("=" * 40)