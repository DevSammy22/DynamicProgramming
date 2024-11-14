#completely mine
# Time Complexity: O(n) — We only need one loop that runs from 2 to n.
def fibonacci(n):

    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]


# Test the function with an example
n = 10
print(f"Fibonacci({n}) = {fibonacci(n)}")