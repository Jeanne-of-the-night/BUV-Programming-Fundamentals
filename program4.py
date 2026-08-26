#PROGRAM 4: EMPLOYEE SCHEDULING & PAYROLL CACULATOR

# Employee and Payroll Data
staff_name = "Alex Smith"
staff_id = "STU-8821"
hours_worked = 15.0 
hourly_rate = 12.00
overtime_hours = 2.0
overtime_rate = 18.00

# Calculation Function
def calculate_payroll():
    gross_pay = (hours_worked * hourly_rate) + (overtime_hours * overtime_rate)
    tax_reserve = gross_pay * 0.10
    net_payout = gross_pay - tax_reserve
    return gross_pay, tax_reserve, net_payout 

# Call function 
gross_pay, tax_reserve, net_payout = calculate_payroll()

#Display Payslip Output
print("Prog 4: Employee Scheduling & Payroll Calculator")
print("=" * 40)
print("STUDENT PAYSLIP")
print("=" * 40)
print("Staff Name:", staff_name, "(ID:", staff_id, ")")
print("Hours Worked:", hours_worked, "hrs @ $", hourly_rate, "/hr")
print("Overtime Hours:", overtime_hours, "hrs @ $", overtime_rate, "/hr")
print("=" * 40)
print("Gross Pay: $", gross_pay)
print("Tax Reserve (10%): -$ ", tax_reserve)
print("=" * 40)
print("NET PAYOUT: $", net_payout)
print("=" * 40)

#PROGRAM 5: FINANCIAL PERFORMANCE & PROFIT/LOSS ESTIMATOR
