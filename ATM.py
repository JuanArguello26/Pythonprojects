# -*- coding: utf-8 -*-

# --- Account Data ---
# This dictionary will store all the user's account information.
# In a real application, this data would come from a secure database.
account_data = {
    "user": "Juanarg",
    "pin": "4271",
    "checking_balance": 1000000.00,
    "savings_balance": 0.00,
    "transaction_history": []
}


# --- Function Definitions ---

def log_transaction(transaction_description):
    """
    Adds a transaction to the history list.
    We limit the history to the last 10 transactions for simplicity.
    """
    history = account_data["transaction_history"]
    history.append(transaction_description)
    # Keep only the last 10 transactions
    if len(history) > 10:
        account_data["transaction_history"] = history[-10:]


def show_balance():
    """Displays the current balance for both checking and savings accounts."""
    print("\n--- ACCOUNT STATEMENT ---")
    print(f"Checking Account: ${account_data['checking_balance']:,.2f}")
    print(f"Savings Account: ${account_data['savings_balance']:,.2f}")
    print("-----------------------\n")
    log_transaction("Balance inquiry")


def withdraw_money():
    """Handles the logic for withdrawing money from the checking account."""
    try:
        amount_to_withdraw = float(input("Enter the amount to withdraw: $"))

        # Validate that the amount is positive
        if amount_to_withdraw <= 0:
            print("Error: The amount must be a positive number.")
            return

        # Check for sufficient funds
        if amount_to_withdraw > account_data["checking_balance"]:
            print("Error: Insufficient funds in your checking account.")
        else:
            # Perform the withdrawal
            initial_balance = account_data["checking_balance"]
            account_data["checking_balance"] -= amount_to_withdraw
            final_balance = account_data["checking_balance"]

            print("\nWithdrawal successful.")
            print(f"Initial balance: ${initial_balance:,.2f}")
            print(f"Final balance: ${final_balance:,.2f}\n")
            log_transaction(f"Withdrawal of ${amount_to_withdraw:,.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter a number.")


def deposit_money():
    """Handles the logic for depositing money into the checking account."""
    try:
        amount_to_deposit = float(input("Enter the amount to deposit: $"))

        # Validate that the amount is positive
        if amount_to_deposit <= 0:
            print("Error: The amount must be a positive number.")
            return

        # Perform the deposit
        initial_balance = account_data["checking_balance"]
        account_data["checking_balance"] += amount_to_deposit
        final_balance = account_data["checking_balance"]

        print("\nDeposit successful.")
        print(f"Initial balance: ${initial_balance:,.2f}")
        print(f"Final balance: ${final_balance:,.2f}\n")
        log_transaction(f"Deposit of ${amount_to_deposit:,.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter a number.")


def transfer_to_savings():
    """Handles logic for transferring money from checking to savings."""
    try:
        amount_to_transfer = float(input("Enter the amount to transfer to savings: $"))

        # Validate that the amount is positive
        if amount_to_transfer <= 0:
            print("Error: The amount must be a positive number.")
            return

        # Check for sufficient funds in the checking account
        if amount_to_transfer > account_data["checking_balance"]:
            print("Error: Insufficient funds to make the transfer.")
        else:
            # Perform the transfer
            account_data["checking_balance"] -= amount_to_transfer
            account_data["savings_balance"] += amount_to_transfer

            print("\nTransfer to savings successful.")
            show_balance()  # Show updated balances
            log_transaction(f"Transfer to savings of ${amount_to_transfer:,.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter a number.")


def show_transaction_history():
    """Displays the user's last 10 transactions."""
    print("\n--- TRANSACTION HISTORY ---")
    history = account_data["transaction_history"]
    if not history:
        print("No recent transactions to display.")
    else:
        for transaction in history:
            print(f"- {transaction}")
    print("---------------------------\n")


def show_menu():
    """
    Displays the main menu and handles user choices until they decide to exit.
    """
    while True:
        print("\n--- ATM MAIN MENU ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transfer to Savings")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Please select an option (1-6): ")

        if choice == '1':
            show_balance()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            transfer_to_savings()
        elif choice == '5':
            show_transaction_history()
        elif choice == '6':
            print("\nThank you for using our ATM. Have a great day!")
            break
        else:
            print("Invalid option. Please try again.")

        # Pause before showing the menu again
        input("Press Enter to continue...")


def login():
    """
    Handles the user login process.
    Allows for a limited number of attempts.
    """
    login_attempts = 0
    max_attempts = 3

    while login_attempts < max_attempts:
        username_input = input("Username: ")
        pin_input = input("PIN: ")

        # Check if credentials are correct
        if username_input == account_data["user"] and pin_input == account_data["pin"]:
            print("\nAccess granted! Welcome, Juan Esteban.")
            return True
        else:
            login_attempts += 1
            remaining_attempts = max_attempts - login_attempts
            print(f"Incorrect username or PIN. You have {remaining_attempts} attempts left.")

    print("You have exceeded the number of attempts. The program will now close.")
    return False


# --- Main Program Execution ---
def main():
    """Main function to run the ATM program."""
    print("--- Welcome to the Trusty ATM ---")
    if login():
        show_menu()


# This makes sure the program starts running from the main function
if __name__ == "__main__":
    main()

