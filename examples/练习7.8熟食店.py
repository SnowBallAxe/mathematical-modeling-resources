sandwich_orders = [
    "Club Sandwich",
    "BLT Sandwich",
    "Ham and Cheese Sandwich",
    "Grilled Cheese Sandwich",
    "Tuna Sandwich",
]
finished_sandwiches = []

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"I made your {made_sandwich}.")
    finished_sandwiches.append(made_sandwich)

for sandwich in finished_sandwiches:
    print(f"\n{sandwich}")
