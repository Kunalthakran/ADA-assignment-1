# Importing all necessary libraries

import time
import random
import matplotlib.pyplot as plt
from functools import lru_cache

# Task 1: Algorithm Growth Observation


def constant_time(n):
    return n * 2


def linear_time(n):
    s = 0
    for i in range(n):
        s += i
    return s


def quadratic_time(n):
    s = 0
    for i in range(n):
        for j in range(n):
            s += i + j
    return s


def logarithmic_time(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count


# Measuring Execution Time
input_sizes = [10, 100, 500, 1000]

functions = [
    ("Constant Time", constant_time),
    ("Linear Time", linear_time),
    ("Quadratic Time", quadratic_time),
    ("Logarithmic Time", logarithmic_time)
]

plt.figure()

for label, func in functions:
    times = []

    for n in input_sizes:
        start = time.time()
        func(n)
        end = time.time()

        times.append(end - start)

    plt.plot(input_sizes, times, label=label)

plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.title("Algorithm Growth Comparison")
plt.legend()
plt.show()


# Task 2: Best, Average and Worst Case Analysis

def linear_search(arr, key):
    for i in arr:
        if i == key:
            return True
    return False


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return False


sizes = [100, 500, 1000]

linear_times = []
binary_times = []

for n in sizes:
    arr = sorted(random.sample(range(1, n * 5), n))

    start = time.time()
    linear_search(arr, arr[n // 2])
    linear_times.append(time.time() - start)

    start = time.time()
    binary_search(arr, arr[n // 2])
    binary_times.append(time.time() - start)


plt.plot(sizes, linear_times, label="Linear Search")
plt.plot(sizes, binary_times, label="Binary Search")

plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.title("Linear Search vs Binary Search")
plt.legend()
plt.show()


# Task 3: Recursion and Recurrence Validation

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci Recursive
fib_calls = 0


def fibonacci_recursive(n):
    global fib_calls
    fib_calls += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Fibonacci using Dynamic Programming
fib_dp_calls = 0


@lru_cache(None)
def fibonacci_dp(n):
    global fib_dp_calls
    fib_dp_calls += 1

    if n <= 1:
        return n

    return fibonacci_dp(n - 1) + fibonacci_dp(n - 2)


# Comparison
n = 10

fib_calls = 0
start = time.time()
fibonacci_recursive(n)
t1 = time.time() - start

fib_dp_calls = 0
start = time.time()
fibonacci_dp(n)
t2 = time.time() - start

print("Naive Fibonacci: Calls =", fib_calls, "Time =", t1)
print("DP Fibonacci: Calls =", fib_dp_calls, "Time =", t2)


# Task 4: Solving Recurrences through Code

# T(n) = T(n/2) + n

calls1 = 0


def recurrence1(n):
    global calls1
    calls1 += 1

    if n <= 1:
        return 1

    return recurrence1(n // 2) + n


# T(n) = 2T(n/2) + n

calls2 = 0


def recurrence2(n):
    global calls2
    calls2 += 1

    if n <= 1:
        return 1

    return recurrence2(n // 2) + recurrence2(n // 2) + n


n = 1024

calls1 = 0
recurrence1(n)
print("T(n) = T(n/2) + n -> Calls:", calls1)

calls2 = 0
recurrence2(n)
print("T(n) = 2T(n/2) + n -> Calls:", calls2)

