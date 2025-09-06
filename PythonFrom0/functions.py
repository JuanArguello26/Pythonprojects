

def perform_calculation(operation, num1, num2):
    """
    Performs a calculation based on the operation provided.

    Args:
        operation (str): The name of the operation ('add', 'subtract', 'multiply', 'divide').
        num1 (float or int): The first number.
        num2 (float or int): The second number.

    Returns:
        The result of the calculation or an error message string.
    """
    # Use if/elif/else to check which operation to perform.
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        # Handle the special case of division by zero.
        if num2 == 0:
            return "Error: Cannot divide by zero."
        else:
            return num1 / num2
    else:
        # Handle cases where an unknown operation is provided.
        return "Error: Invalid operation specified."

# --- Example Usage ---

# Example 1: Multiplication (as requested in the exercise)
result_multiply = perform_calculation("multiply", 5, 4)
print(f"The result of multiplying 5 by 4 is: {result_multiply}") # Expected output: 20

# Example 2: Addition
result_add = perform_calculation("add", 10, 7)
print(f"The result of adding 10 and 7 is: {result_add}") # Expected output: 17

# Example 3: Subtraction
result_subtract = perform_calculation("subtract", 15, 3)
print(f"The result of subtracting 3 from 15 is: {result_subtract}") # Expected output: 12

# Example 4: Division
result_divide = perform_calculation("divide", 100, 5)
print(f"The result of dividing 100 by 5 is: {result_divide}") # Expected output: 20.0

# Example 5: Division by zero (error handling)
result_div_zero = perform_calculation("divide", 50, 0)
print(f"Trying to divide by zero: {result_div_zero}") # Expected output: Error message

# Example 6: Invalid operation (error handling)
result_invalid = perform_calculation("power", 2, 3)
print(f"Trying an invalid operation: {result_invalid}") # Expected output: Error message
