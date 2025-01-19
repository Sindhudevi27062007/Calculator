def calculator():
    # Ask the user for the numbers first
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Display the menu of operations
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        # Take input from the user for operation
        operation = input("Enter choice (1/2/3/4): ")

        # Perform the operation based on the user's choice
        if operation == '1':
            result = num1 + num2
        elif operation == '2':
            result = num1 - num2
        elif operation == '3':
            result = num1 * num2
        elif operation == '4':
            if num2 == 0:
                result = "Error! Division by zero."
            else:
                result = num1 / num2
        else:
            result = "Invalid input! Please choose a valid operation."

        # Display the result
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter valid numerical values.")

# Call the calculator function to use it
calculator()
