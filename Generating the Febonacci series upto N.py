def generate_fibonacci(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage:
n = int(input("Enter the number of terms: "))
fib_series = generate_fibonacci(n)
print(f"Fibonacci series up to {n} terms: {fib_series}")
