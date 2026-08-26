inventory = {
    "Coffee": {
        "item_id": "ITEM101",
        "stock": 3,
        "threshold": 5
    },
    "Tea": {
        "item_id": "ITEM102",
        "stock": 10,
        "threshold": 5
    },
    "Sandwich": {
        "item_id": "ITEM103",
        "stock": 2,
        "threshold": 5
    }
}

item_name = input("Item Name: ").capitalize()

item_id = inventory[item_name]["item_id"]
stock = inventory[item_name]["stock"]
threshold = inventory[item_name]["threshold"]

if stock < threshold:
    status = "REORDER!"
else:
    status = "OK"

print("===== INVENTORY CARD =====")
print(f"Item ID: {item_id}")
print(f"Item Name: {item_name}")
print(f"Stock: {stock}")
print(f"Threshold: {threshold}")
print(f"Status: {status}")