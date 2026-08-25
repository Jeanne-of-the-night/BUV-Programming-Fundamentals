# DATA STORAGE 
customers_data = [
    {"id": "C000001", "name": "Aemeathreiko", "points": 99, "tier": "Bronze"},
    {"id": "C000002", "name": "Bouncy", "points": 100, "tier": "Silver"},
    {"id": "C000003", "name": "Creepy", "points": 300, "tier": "Gold"},
]

# Exchange rates (base on 1 USD). Data taken in 24/08/2026
rates = {
    "USD": 1.0,
    "EUR": 0.86,
    "GBP": 0.73,
    "JPY": 158.89,
    "AUD": 1.40,
    "CNY": 6.72,
    "VND": 26172.0
}

# Functions
# Functions for Customer Management, Loyalty and Tiered
def tier_check(points):
    """Checks the tier of a customer based on their points. Using if-elif-else."""
    if points >= 300:
        return "Gold"
    elif points >= 100:
        return "Silver"
    else:
        return "Bronze"


def customer_view():
    """Displays the list of all customers. Using for loop."""
    print("Customer List:")
    for customer in customers_data:
        print(f"ID: {customer['id']}, Name: {customer['name']}, Points: {customer['points']}, Tier: {customer['tier']}")


def customer_register():
    """Registers a new customer. Using input() and appending to the list."""
    new_id = input("Enter new customer ID (e.g., C110307): ")
    for customer in customers_data:
        if customer['id'] == new_id:
            print("Customer ID already exists. Registration failed.")
            return

    new_name = input("Enter customer name: ")
    new_customer = {"id": new_id, "name": new_name, "points": 0, "tier": "Bronze"}
    customers_data.append(new_customer)
    print(f"Customer {new_name} registered successfully.")


def add_points():
    """Adds points to a customer's account. Using input() and updating the list."""
    customer_id = input("Enter customer ID to add points: ")

    for customer in customers_data:
        if customer['id'] == customer_id:
            amount = int(input("Enter points to add (1 point per $1 spent, rounded down): "))
            points_earned = int(amount)
            customer['points'] += points_earned
            customer['tier'] = tier_check(customer['points'])
            print(f"Added {points_earned} points to {customer['name']}. New points: {customer['points']}, New tier: {customer['tier']}")
            return

    print("Customer ID not found. Points addition failed.")


def points_redeem():
    """Redeems points for a customer. Using input() and updating the list."""
    customer_id = input("Enter customer ID to redeem points: ")

    for customer in customers_data:
        if customer['id'] == customer_id:
            points_to_redeem = int(input("Enter points to redeem: "))
            if points_to_redeem > customer['points']:
                print(f"Insufficient points. {customer['name']} has only {customer['points']} points.")
                return
            customer['points'] -= points_to_redeem
            customer['tier'] = tier_check(customer['points'])
            print(f"Redeemed {points_to_redeem} points from {customer['name']}. New points: {customer['points']}, New tier: {customer['tier']}")
            return

    print("Customer ID not found. Points redemption failed.")

#Functions for Currency Conversion
def view_exchange_rates():
    """Displays the current exchange rates. Using for loop."""
    print("Current Exchange Rates (base on 1 USD):")
    for currency in rates:
        print(f"{currency}: {rates[currency]}")


def currency_convert():
    """Converts an amount from one currency to another. Using input() and calculations."""
    amount = float(input("Enter amount to convert: "))
    from_currency = input("Enter the currency to convert from (only available for USD, EUR, GBP, JPY, AUD, CNY, VND): ").upper()
    to_currency = input("Enter the currency to convert to (only available for USD, EUR, GBP, JPY, AUD, CNY, VND): ").upper()

    if amount < 0:
        print("Amount cannot be negative. Conversion failed.")
        return
    
    if from_currency in rates and to_currency in rates:
        usd_amount = amount / rates[from_currency]  # Convert to USD first
        converted_amount = usd_amount * rates[to_currency]  # Then convert to target currency
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    else:
        print("Invalid currency code. Conversion failed.")


def cross_border_fee():
    """Calculates the cross-border fee for a transaction. Using input() and calculations."""
    amount = float(input("Enter transaction amount in USD: "))
    if amount < 0:
        print("Amount cannot be negative. Fee calculation failed.")
        return
    fee_percentage = 0.02  # 2% fee
    fee = amount * fee_percentage
    total_amount = amount + fee
    print(f"Transaction Amount: ${amount:.2f}, Cross-Border Fee: ${fee:.2f}, Total Amount: ${total_amount:.2f}")


# Main Menu

def main_menu():
    """Displays the main menu and handles user input. Using while loop and if-elif-else."""
    while True:
        print("\n--- Main Menu ---")
        print("1. View Customers")
        print("2. Register Customer")
        print("3. Add Points")
        print("4. Redeem Points")
        print("5. View Exchange Rates")
        print("6. Currency Conversion")
        print("7. Cross-Border Fee Calculation")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            customer_view()
        elif choice == '2':
            customer_register()
        elif choice == '3':
            add_points()
        elif choice == '4':
            points_redeem()
        elif choice == '5':
            view_exchange_rates()
        elif choice == '6':
            currency_convert()
        elif choice == '7':
            cross_border_fee()
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ = "__main__":
    main_menu()
