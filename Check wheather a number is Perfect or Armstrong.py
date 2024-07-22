def is_perfect_number(n):
    if n < 1:
        return False
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n

def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum([int(digit) ** num_digits for digit in num_str])
    return sum_of_powers == n

# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is a perfect number
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

# Check if the number is an Armstrong number
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
