import sys
import time

# Increase recursion limit to support deep recursion up to n = 1000
sys.setrecursionlimit(3000)

# Global counter and memoization table for Algorithm B
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


# Fix 2: Calculate Fibonacci values using a loop
def fib_iterative(n):
    if n == 0:
        return 0

    previous = 0
    current = 1

    for i in range(2, n + 1):
        next_value = previous + current
        previous = current
        current = next_value

    return current


if __name__ == "__main__":

  print("\n--- Starting Part 2 Experiments for Algorithm B ---")
  test_values_b = [10, 50, 100, 200, 500, 1000]

  for n in test_values_b:
    calls_b = 0
    fibtable.clear()  # Clear table before each run as required

    start_time = time.perf_counter()
    ans = fib_b(n)
    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(
        f"n = {n:4d} | Calls: {calls_b:5,d} | Time: {elapsed:.6f} seconds"
    )

  # Part 4 Fix 2: Test the iterative algorithm at n = 1000
  print("\n--- Part 4 Fix 2: Iterative Fibonacci ---")
  print("F(1000):", fib_iterative(1000))