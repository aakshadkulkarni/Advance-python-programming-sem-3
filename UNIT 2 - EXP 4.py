# Efficient Fibonacci using Memoization

# Method 1: Normal Recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Method 2: Fibonacci using Memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


# Taking input from user
n = int(input("Enter the value of n: "))

# Method 1
print("\nMethod 1: Normal Recursion")
result1 = fibonacci_recursive(n)
print("Fibonacci number:", result1)


# Method 2
print("\nMethod 2: Memoization")
result2 = fibonacci_memo(n)
print("Fibonacci number:", result2)
