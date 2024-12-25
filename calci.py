def get_number(prompt):
    """
    Prompts the user to input a number, validates input, and returns the number.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    """
    Prompts the user to select an operation and returns the operation symbol.
    """
    operations = {
        '1': 'Addition (+)',
        '2': 'Subtraction (-)',
        '3': 'Multiplication (*)',
        '4': 'Division (/)',
    }
    
    print("\nChoose an operation:")
    for key, desc in operations.items():
        print(f"{key}. {desc}")
    
    while True:
        choice = input("Enter the operation number (1-4): ")
        if choice in operations:
            return choice
        print("Invalid choice! Please select a number between 1 and 4.")

def calculate(num1, num2, operation):
    """
    Performs the chosen arithmetic operation and returns the result.
    """
    if operation == '1':  # Addition
        return num1 + num2
    elif operation == '2':  # Subtraction
        return num1 - num2
    elif operation == '3':  # Multiplication
        return num1 * num2
    elif operation == '4':  # Division
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

def main():
    """
    Main function to orchestrate the calculator operations.
    """
    print("Welcome to the Simple Calculator!")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()
    
    result = calculate(num1, num2, operation)
    
    operation_symbols = {'1': '+', '2': '-', '3': '*', '4': '/'}
    symbol = operation_symbols[operation]
    
    print(f"\nResult: {num1} {symbol} {num2} = {result}")

# Run the calculator program
if __name__ == "__main__":
    main()
