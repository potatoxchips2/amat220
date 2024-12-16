import math

# Define the function f(k)
def f(k):
    return (-1)**k / ((2*k + 1) * (3**(2*k + 1)))

# Define the S_n function (sum of f(k) for k = 1 to n)
def S_n(n):
    return 4 * (sum(f(k) for k in range(1, n + 1)))

# Value of pi
pi_value = math.pi

# Define N (from Part 3) and the range of n
N = 100  # Example value of N
results = []

# Calculate S_n and |S_n - pi| for n = 1 to N + 2
for n in range(1, N + 3):  # 1 <= n <= N + 2
    sn = S_n(n)
    diff = abs(sn - pi_value)
    results.append((n, sn, diff))

# Output the results
for n, sn, diff in results:
    print(f"n = {n}, S_n = {sn}, |S_n - pi| = {diff}")

# You can save or print these results as needed (PDF, screenshot, etc.)
