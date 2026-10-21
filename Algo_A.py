import time

# Global counter for Algorithm A function calls
calls_a = 0


def fib_a(n):
  global calls_a
  calls_a += 1
  if n == 0 or n == 1:
    return n
  return fib_a(n - 1) + fib_a(n - 2)


if __name__ == "__main__":

  print("\n--- Starting Part 2 Experiments for Algorithm A ---")
  test_values_a = [5, 10, 15, 20, 25, 30, 35]

  for n in test_values_a:
    calls_a = 0
    start_time = time.perf_counter()
    ans = fib_a(n)
    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(
        f"n = {n:2d} | Calls: {calls_a:10,d} | Time: {elapsed:.6f} seconds"
    )

    # Stop condition: if a run takes longer than 60 seconds
    if elapsed > 60.0:
      print(
          f"Run took longer than 60 seconds at n = {n}. Stopping Algorithm A."
      )
      break