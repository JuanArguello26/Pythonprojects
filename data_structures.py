# -*- coding: utf-8 -*-

def grocery_list_program():
    """
    Main function to run the interactive grocery list program.
    """
    # Initialize an empty list to store grocery items.
    grocery_list = []

    # Use a 'while True' loop to keep the program running until the user exits.
    while True:
        # --- Display Menu ---
        print("\n--- Grocery List Menu ---")
        print("1. Add an item to the list")
        print("2. Print the current list")
        print("3. Exit the program")

        # Ask the user for their choice.
        choice = input("Please enter your choice (1, 2, or 3): ")

        # --- Process User's Choice ---

        # Option 1: Add an item
        if choice == '1':
            item = input("What would you like to add to the list? ")
            grocery_list.append(item)
            print(f"'{item}' has been added to your list.")

        # Option 2: Print the list
        elif choice == '2':
            print("\n*** YOUR LIST ***")
            # Check if the list is empty before trying to print it.
            if not grocery_list:
                print("Your list is currently empty.")
            else:
                # Use a for loop with enumerate to print items with a number.
                for index, item in enumerate(grocery_list, start=1):
                    print(f"{index}. {item}")
            print("*****************")

        # Option 3: Exit the program
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break  # This statement exits the 'while' loop.

        # Handle invalid input
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# --- Start the program ---
# We call the main function to run everything.
grocery_list_program()
