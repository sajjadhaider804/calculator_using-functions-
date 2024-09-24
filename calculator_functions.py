# calculator using functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            return

        if operation == '1':
            print(f"Result: {add(num1, num2)}")
        elif operation == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif operation == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif operation == '4':
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    calculator()
