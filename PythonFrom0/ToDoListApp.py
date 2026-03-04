# --- Global Task List ---
# This list will store all the tasks. It's defined globally
# so all functions can access and modify it.
tasks = []


# --- Function to display the menu ---
def display_menu():
    """Prints the main menu options for the user."""
    print("\n--- To-Do List Menu ---")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Delete a task")
    print("4. Exit")
    print("-----------------------")


# --- Function to view all tasks ---
def view_tasks():
    """Displays all the tasks currently in the list."""
    print("\n--- Your Tasks ---")
    # Check if the tasks list is empty.
    if not tasks:
        print("Your to-do list is empty. Add a task to get started!")
    else:
        # Enumerate provides an index and the item, making it easy to display a numbered list.
        # We start the count from 1 for a user-friendly display.
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("------------------")


# --- Function to add a task ---
def add_task():
    """Prompts the user for a new task and adds it to the list."""
    # Get input from the user for the new task description.
    new_task = input("Enter the task you want to add: ")

    # Add the new task to the end of our global 'tasks' list.
    tasks.append(new_task)

    # Provide feedback to the user that the task was added successfully.
    print(f"✅ Task '{new_task}' was added to your list.")


# --- Function to delete a task ---
def delete_task():
    """Shows the current tasks and deletes one selected by the user."""
    # First, show the user the tasks so they know which one to delete.
    view_tasks()

    # If the list is empty, we can't delete anything, so we return early.
    if not tasks:
        return

    try:
        # Ask the user for the number of the task they wish to delete.
        task_number_to_delete = int(input("Enter the number of the task to delete: "))

        # We must check if the entered number corresponds to an actual task.
        # The numbers are 1-based for the user, but the list index is 0-based.
        if 1 <= task_number_to_delete <= len(tasks):
            # Calculate the list index by subtracting 1 from the user's input.
            task_index = task_number_to_delete - 1

            # Use pop() to remove the task at the specified index.
            # We store the removed task to show it in the confirmation message.
            removed_task = tasks.pop(task_index)
            print(f"❌ Task '{removed_task}' was successfully deleted.")
        else:
            # This message shows if the number is out of the valid range.
            print("Invalid task number. Please enter a number from the list.")

    except ValueError:
        # This error occurs if the user enters text instead of a number.
        print("Invalid input. Please enter a number.")


# --- Main Program Loop ---
def main():
    """The main function that runs the application loop."""
    # This loop will run forever until the user chooses to exit.
    while True:
        display_menu()

        # Get the user's choice from the menu.
        user_choice = input("Enter your choice (1-4): ")

        if user_choice == '1':
            view_tasks()
        elif user_choice == '2':
            add_task()
        elif user_choice == '3':
            delete_task()
        elif user_choice == '4':
            print("👋 Goodbye! Thanks for using the To-Do List app.")
            # The 'break' keyword exits the while loop, ending the program.
            break
        else:
            # Handle cases where the user enters an invalid option.
            print("Invalid choice. Please enter a number between 1 and 4.")


# This standard Python construct ensures that the main() function is called
# only when the script is executed directly.
if __name__ == "__main__":
    main()