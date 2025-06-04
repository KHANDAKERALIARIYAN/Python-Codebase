# Recursion

def factorial(n):
    if (n==0 or n==1):
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120

def fibonacci(n):
    if (n==0) or (n==1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # Output: 8