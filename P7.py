vendors = {
    "V001": {
        "Coffee": 3.50,
        "Tea": 2.50,
        "Sandwich": 5.00
    },
    "V002": {
        "Salad": 4.00,
        "Muffin": 2.00,
        "Cookie": 1.50
    },
    "V003": {
        "Cheesecake": 4.50,
        "Smoothie": 3.75,
        "Juice": 3.00
    }
}

vendor_id = input("Vendor ID: ").upper()
item_name = input("Item Name: ").capitalize()
purchase_quantity = int(input("Purchase Quantity: "))
status = input("Status: ").upper()

unit_price = vendors[vendor_id][item_name]

total_cost = purchase_quantity * unit_price

if purchase_quantity > 100:
    print("Purchase quantity cannot exceed 100.")
else:
    total_cost = purchase_quantity * unit_price

    print("===== PURCHASE ORDER =====")
    print(f"Vendor ID: {vendor_id}")
    print(f"Item Name: {item_name}")
    print(f"Quantity: {purchase_quantity}")
    print(f"Unit Price: ${unit_price:.2f}")
    print(f"Total Cost of Goods: ${total_cost:.2f}")
    print(f"Status: {status}")