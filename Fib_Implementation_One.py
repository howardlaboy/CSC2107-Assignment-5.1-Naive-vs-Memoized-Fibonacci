import time

# Algorithm A: Plain recursion
calls_a = 0

def fib_a(n):
    global calls_a
    calls_a += 1

    if n == 0 or n == 1:
        return n
    else:
        return fib_a(n - 1) + fib_a(n - 2)


# Algorithm B: Recursion with memoization
calls_b = 0
fibtable = {}

def fib_b(n):
    global calls_b
    calls_b += 1

    if n in fibtable:
        return fibtable[n]

    if n == 0 or n == 1:
        value = n
    else:
        value = fib_b(n - 1) + fib_b(n - 2)

    fibtable[n] = value
    return value


# Check that both algorithms return the same values
print("Checking Fibonacci values from n = 0 to 20")

print(f"{'n':>2} {'A':>8} {'B':>8}")
for n in range(21):
    calls_a = 0
    calls_b = 0
    fibtable.clear()

    result_a = fib_a(n)
    result_b = fib_b(n)

    print(f"{n:>2} {result_a:>8} {result_b:>8}")

    assert result_a == result_b

print("Both algorithms return the same values.")