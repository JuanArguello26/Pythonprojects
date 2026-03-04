# -*- coding: utf-8 -*-

# --- Main Program Logic ---

# 1. Ask the user to enter some text.
print("Please enter the text you would like to repeat:")
user_text = input()

# 2. Then ask the user to enter how many times they want to print it.
print("\nHow many times would you like to print the text?")

# We use a try-except block to handle cases where the user might not enter a valid number.
try:
    repeat_count = int(input())

    # We should also handle the case where the user enters a negative number.
    if repeat_count < 0:
        print("\nPlease enter a positive number of repetitions.")
    else:
        # 3. Print the text the requested number of times using a 'for' loop.
        print("\n--- Here is your repeated text ---")
        for i in range(repeat_count):
            # The loop will run 'repeat_count' times.
            # In each iteration, we print the user's text.
            print(user_text)

except ValueError:
    # This message is shown if the user's input for the count is not a number.
    print("\nInvalid input. Please enter a whole number for the repetitions.")

print("\n--- Program finished ---")
