
import sys


menu = {
    "Coffee": 3.50,
    "Tea": 2.50,
    "Sandwich": 5.00,
    "Salad": 4.00,
    "Muffin": 2.00,
    "Cookie": 1.50,
    "Cheesecake": 4.50,
    "Smoothie": 3.75,
    "Juice" : 3.00,
    "Espresso": 2.75
}

PROMO_CODES = {
    "DISCOUNT10": 0.10,  # 10% discount
    "STUDENT90": 0.20,  # 20% discount
    "FREEDRINK": 1.00     # Free drink (up to $3.50)
}



order = input("Enter the items you want to order (Exp: Coffee 2, Tea 1, Sandwich 1): ")
print("Order received. Processing your order...")
promo_code = input("Enter a promo code (if applicable): ").upper()


order_list = [{item.split()[0].strip().capitalize(): int(item.split()[1])} for item in order.split(",") if item.split()[0].strip().capitalize() in menu]

if not order_list:
    print("No valid items were entered. Please enter at least one valid item from the menu to proceed.")
    sys.exit()


def calculate_price(item, quantity):
    """Calculates the total price for a given item and quantity. Using input() and calculations."""
    if item in menu:
        total_price = menu[item] * quantity
        return total_price
    else:
        pass  # Item not found in the menu, ignore it


def calculate_total(order_list):
    total_price = 0
    for order in order_list:
        for item, quantity in order.items():
            total_price += calculate_price(item, quantity)
    return total_price


print("==============================================")
print("          CAMPUS CAFE POS TERMINAL            ")
print("==============================================")
print(f"{'Item':<18} {'Qty':^5} {'Price':>9} {'Total':>10}")
print("----------------------------------------------")

sub_total = calculate_total(order_list)
# Line Items
for i, item_dict in enumerate(order_list, start=1):
    for item, qty in item_dict.items():
        total = calculate_price(item, qty)
        item_label = f"{i}. {item}"
        
        # Format columns cleanly using aligned numbers
        print(f"{item_label:<18} {qty:^5} {f'${menu[item]:.2f}':>9} {f'${total:.2f}':>10}")

# Prices
print("----------------------------------------------")
print(f"{'Subtotal:':<33} {f'${sub_total}':>10}")
if promo_code in PROMO_CODES:
    discount = PROMO_CODES[promo_code]
    discount_amount = sub_total * discount
    print(f"{'Discount:':<33} {f'-${discount_amount:.2f}':>10}")
print(f"{'Tax (5%):':<33} {f'${sub_total * 0.05:.2f}':>10}")
print("==============================================")
print(" [1] Complete Sale | [2] Cancel Order")

# Footer
print("----------------------------------------------")
print(f"{'TOTAL DUE:':<33} {f'${sub_total - discount_amount + sub_total * 0.05:.2f}':>10}")
print("==============================================")
print(" [1] Complete Sale | [2] Cancel Order")