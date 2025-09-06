# invsee.py
# A simple inventory management system for a computer hardware store.

def view_inventory(inventory):
    """
    Displays the current inventory levels for all items and the total count.
    - inventory: A dictionary containing the item names as keys and quantities as values.
    """
    print("\n--- Current Inventory ---")
    total_items = 0
    if not inventory:
        print("The inventory is currently empty.")
    else:
        # Iterate through the inventory dictionary to display each item and its quantity.
        for item, quantity in inventory.items():
            print(f"{item.capitalize()}: {quantity}")  # Shows quantity for each product
            total_items += quantity

    print("-------------------------")
    # Display the total number of all items combined.
    print(f"Total number of all items: {total_items}")
    print("-------------------------\n")


def add_stock(inventory):
    """
    Adds a specified quantity of an item to the inventory.
    This function already works by product type, as it asks for the item's name.
    - inventory: The inventory dictionary to be updated.
    """
    try:
        # Get user input for the item name and quantity.
        item_name = input("Enter the name of the item to add (e.g., cpu): ").lower()
        quantity = int(input(f"Enter the quantity of '{item_name}' to add: "))

        if quantity <= 0:
            print("Error: Please enter a quantity greater than zero.")
            return

        # Update the inventory. If the item already exists, add to its quantity.
        inventory[item_name] = inventory.get(item_name, 0) + quantity
        print(f"\nSuccessfully added {quantity} of '{item_name}'.")

    except ValueError:
        print("\nError: Invalid quantity. Please enter a whole number.")


def remove_stock(inventory):
    """
    Removes a specified quantity of an item from the inventory.
    This function already works by product type.
    - inventory: The inventory dictionary to be updated.
    """
    try:
        # Get user input for the item name and quantity to remove.
        item_name = input("Enter the name of the item to remove: ").lower()

        if item_name not in inventory:
            print(f"\nError: Item '{item_name}' not found in inventory.")
            return

        quantity = int(input(f"Enter the quantity of '{item_name}' to remove: "))

        if quantity <= 0:
            print("Error: Please enter a quantity greater than zero.")
            return

        if quantity > inventory[item_name]:
            print(f"\nError: Not enough stock. You only have {inventory[item_name]} of '{item_name}'.")
        else:
            inventory[item_name] -= quantity
            print(f"\nSuccessfully removed {quantity} of '{item_name}'.")

    except ValueError:
        print("\nError: Invalid quantity. Please enter a whole number.")


# --- NEW FUNCTION ---
def check_specific_item(inventory):
    """
    Checks and displays the quantity of a single, specific item.
    - inventory: The inventory dictionary.
    """
    item_name = input("Enter the name of the item to check: ").lower()

    # Get the quantity from the inventory. Use .get() to return 0 if not found.
    quantity = inventory.get(item_name)

    if quantity is not None:
        print(f"\n---> Stock for '{item_name.capitalize()}': {quantity} units.")
    else:
        print(f"\n---> Item '{item_name}' not found in inventory.")


def main():
    """
    Main function to run the inventory management program.
    """
    hardware_inventory = {
        'monitors': 20,
        'graphics cards': 15,
        'fans': 50,
        'ram modules': 45,
        'ssd drives': 30,
        'cpu': 25  # Added CPU for variety
    }

    while True:
        # The menu is updated with the new option.
        print("\n--- Inventory Management Menu ---")
        print("1. View all inventory")
        print("2. Add stock (by product type)")
        print("3. Remove stock (by product type)")
        print("4. Check stock of a specific item")  # New option
        print("5. Exit")

        user_choice = input("Please enter your choice (1-5): ")

        if user_choice == '1':
            view_inventory(hardware_inventory)
        elif user_choice == '2':
            add_stock(hardware_inventory)
        elif user_choice == '3':
            remove_stock(hardware_inventory)
        elif user_choice == '4':
            # Call the new function.
            check_specific_item(hardware_inventory)
        elif user_choice == '5':
            print("Exiting the inventory program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()