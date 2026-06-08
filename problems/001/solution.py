# Problem 1 — Multiples of 3 or 5
# Find the sum of all multiples of 3 or 5 below 1000.

solution = 0

for index in range(1000):
    if index % 3 == 0 or index % 5 == 0:
        solution += index

print(solution)
