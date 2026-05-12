# -*- coding: utf-8 -*-

# --- Main Program Logic ---

# 1. Print a message asking the user for a number between 1 and 100.
print("Please enter a number between 1 and 100.")

# We use a try-except block to gracefully handle cases where the user
# might enter text instead of a number.
try:
    # Get the number from the user and convert it to an integer.
    user_number = int(input())

    # a) Check if the number is less than 1.
    if user_number < 1:
        print("Please enter a number greater than 0.")

    # b) Check if the number is greater than 100.
    elif user_number > 100:
        print("Please enter a number less than or equal to 100.")

    # c) If the number is valid (between 1 and 100, inclusive).
    else:
        # Note: The original request had a mix of English and Spanish.
        # I will write the final message in Spanish as requested.
        print(f"¡Muy bien! El {user_number} es una gran opción.")

except ValueError:
    # This message will be shown if the user enters something that is not a number.
    print("Invalid input. Please enter a valid number.")
