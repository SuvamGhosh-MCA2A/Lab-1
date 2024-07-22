def find_factors(number):
    factors = []
    # Loop through all numbers from 1 to the number itself
    for i in range(1, number + 1):
        # Check if i divides the number without leaving a remainder
        if number % i == 0:
            factors.append(i)  # i is a factor, so add it to the list of factors
    return factors

# Input from the user
num = int(input("Enter a number: "))

# Call the function to find factors
result = find_factors(num)

# Display the factors
print(f"The factors of {num} are: {result}")
