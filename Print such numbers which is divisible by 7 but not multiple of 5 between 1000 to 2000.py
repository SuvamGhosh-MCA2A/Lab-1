def find_numbers():
    results = []
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            results.append(num)
    return results

# Display the results
numbers = find_numbers()
for number in numbers:
    print(number)
