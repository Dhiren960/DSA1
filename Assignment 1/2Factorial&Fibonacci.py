def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fib_naive(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

n = int(input("Enter n (>=0): "))

print("Factorial:", factorial(n))
print("Fibonacci (Naive):", fib_naive(n))
print("Fibonacci (Memoization):", fib_memo(n))

print("Factorial Time Complexity: O(n)")
print("Factorial Space Complexity: O(n)")
print("Naive Fibonacci Time Complexity: O(2^n)")
print("Naive Fibonacci Space Complexity: O(n)")
print("Memoized Fibonacci Time Complexity: O(n)")
print("Memoized Fibonacci Space Complexity: O(n)")