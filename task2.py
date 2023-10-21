from operator import add, mul, truediv, pow

# Create a dictionary to store arithmetic operations and corresponding lambda functions
arithmetic_operations = {
    '1': lambda a, b: add(a, b),
    '2': lambda a, b: mul(a, b),
    '3': lambda a, b: truediv(a, b) if b != 0 else 'Error: Division by zero',
    '4': lambda a, b: pow(a, b)
}

# Prompt the user to select an arithmetic operation
operation = input("Please chose the task you want to perform:\n1. Addition\n2. Multiplication\n3. Division\n4. Exponentiation\nUser Input: ")

# Split the input numbers into a list and convert them to integers
numbers = list(map(int, input("Please enter two numbers for addition, comma separated\nUser Input: ").split(',')))

# Perform the selected arithmetic operation on the input numbers
result = arithmetic_operations[operation](numbers[0], numbers[1])

# Print the result
print(result)