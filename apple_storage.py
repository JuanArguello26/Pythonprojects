    # -*- coding: utf-8 -*-

    # --- Initial Store Setup ---
    # We define the initial number of apples and their price.
    initial_apples_available = 20
    apple_price = 5

    # --- Main Program Logic ---

    # 1. Print a message, welcoming the user and asking for their name.
    print("Welcome to the Apple Store! What is your name?")

    # 2. Now the user must enter their name.
    user_name = input()

    # 3. Print message, greeting the user by name, and indicating the stock and price.
    print(f"\nHello, {user_name}! We currently have {initial_apples_available} apples available.")
    print(f"Each apple costs ${apple_price}.")

    # 4. Print a message, asking the user how many apples they want to buy.
    print("\nHow many apples would you like to buy?")

    # 5. Now the user must enter how many apples they want.
    # We use a try-except block to handle cases where the user might not enter a number.
    try:
        apples_to_buy = int(input())

        # We should also check if the user is trying to buy more apples than available.
        if apples_to_buy > initial_apples_available:
            print(f"\nSorry, we only have {initial_apples_available} apples available.")
            print("Please restart the program to try again.")
        elif apples_to_buy < 0:
            print("\nYou can't buy a negative number of apples!")
        else:
            # 6. Print a message indicating how many apples the user bought, and what the total price was.
            total_price = apples_to_buy * apple_price
            print(f"\nGreat! You bought {apples_to_buy} apples for a total price of ${total_price}.")

            # 7. Finally, print a message indicating how many apples were available after the sale.
            remaining_apples = initial_apples_available - apples_to_buy
            print(f"There are now {remaining_apples} apples left in the store.")

    except ValueError:
        print("\nThat's not a valid number. Please run the program again and enter a number.")

    print("\nThank you for visiting!")
