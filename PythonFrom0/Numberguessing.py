# Import the 'random' module, which contains functions for generating random numbers.
import random

# --- Game Setup ---

# Define the lower and upper bounds for the secret number.
lower_bound = 1
upper_bound = 100

# Generate a random integer between the lower and upper bounds (inclusive).
# This is the number the player needs to guess.
secret_number = random.randint(lower_bound, upper_bound)

# Initialize a variable to store the player's guess. We start it at 0.
player_guess = 0

# Initialize a counter for the number of attempts the player makes.
guess_count = 0

# --- Welcome Message ---
print("--- Welcome to the Number Guessing Game! ---")
print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
print("Try to guess it!")

# --- Main Game Loop ---

# This 'while' loop will continue to run as long as the player's guess
# is not equal to the secret number.
while player_guess != secret_number:

    # Prompt the player to enter their guess.
    # The input() function reads a line from the console as a string.
    try:
        player_guess = int(input("Enter your guess: "))
    except ValueError:
        # If the player enters something that is not a number (like 'abc'),
        # the int() conversion will fail and raise a ValueError.
        # This 'except' block catches that error and prints a friendly message.
        print("Please enter a valid number.")
        # The 'continue' keyword skips the rest of this loop iteration
        # and goes back to the beginning to ask for input again.
        continue

    # Increment the guess counter after each valid attempt.
    guess_count += 1

    # --- Compare Guess and Provide Feedback ---

    # Check if the guess is lower than the secret number.
    if player_guess < secret_number:
        print("Too low! Try again.")

    # Check if the guess is higher than the secret number.
    elif player_guess > secret_number:
        print("Too high! Try again.")

    # If the guess is neither lower nor higher, it must be correct.
    # This 'else' block runs when the player guesses the right number.
    else:
        print(f"\n🎉 Congratulations! You guessed the number!")
        print(f"The secret number was {secret_number}.")
        print(f"It took you {guess_count} guesses to win.")

# This line prints after the 'while' loop has finished.
print("\nThanks for playing!")