def swap_numbers(a, b):
    return b, a

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swapping the numbers
num1, num2 = swap_numbers(num1, num2)

# Display the results
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)