inventory = {}

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add a product")
    print("2. Update stock quantity")
    print("3. Search by category")
    print("4. Total inventory value")
    print("5. Low-stock alerts")
    print("6. Summary report by category")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter product name: ").strip().title()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price (Rs): "))
        category = input("Enter category: ").strip().title()
        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative!")
        else:
            inventory[name] = {
                "quantity": quantity,
                "price": price,
                "category": category
            }
            print("Product added successfully!")
    elif choice == "2":
        name = input("Enter product name: ").strip().title()
        if name in inventory:
            quantity = int(input("Enter new stock quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative!")
            else:
                inventory[name]["quantity"] = quantity
                print("Stock updated successfully!")
        else:
            print("Product not found!")
    elif choice == "3":
        category = input("Enter category to search: ").strip().title()
        found = False
        for name, details in inventory.items():
            if details["category"] == category:
                print(
                    f"{name} - Quantity: {details['quantity']}, "
                    f"Price: Rs {details['price']}"
                )
                found = True
        if not found:
            print("No products found in this category.")
    elif choice == "4":
        total_value = 0
        for details in inventory.values():
            total_value += details["quantity"] * details["price"]
        print(f"Total inventory value: Rs {total_value:.2f}")
    elif choice == "5":
        threshold = int(input("Enter low-stock threshold: "))
        found = False
        print(f"\nLow stock (< {threshold}):")
        for name, details in inventory.items():
            if details["quantity"] < threshold:
                print(f"  - {name} ({details['quantity']} left)")
                found = True
        if not found:
            print("No low-stock products.")
    elif choice == "6":
        if not inventory:
            print("Inventory is empty!")
        else:
            categories = {}
            for name, details in inventory.items():
                category = details["category"]
                if category not in categories:
                    categories[category] = []
                categories[category].append((name, details))
            for category, products in categories.items():
                print(f"\nCategory: {category}")

                for name, details in products:
                    print(
                        f"  {name:<12} x{details['quantity']}  "
                        f"@ Rs {details['price']:g}"
                    )
    elif choice == "7":
        print("Exiting Inventory Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")