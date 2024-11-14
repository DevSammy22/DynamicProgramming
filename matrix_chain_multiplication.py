#mine
import sys
def matrix_chain_multiplication(dims):
    n = len(dims) - 1
    opt = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, (n + 1)):
        for i in range(1, (n - length) + 2):
            j = i + (length - 1)
            #opt[i][j] = float("inf")
            opt[i][j] = sys.maxsize # to set the infinity initially

            for k in range(i, j):
                cost_of_multiplication = opt[i][k] + opt[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost_of_multiplication < opt[i][j]:
                    opt[i][j] = cost_of_multiplication
                    split[i][j] = k

    return opt[1][n], split


def print_optimal_order(split, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_order(split, i, split[i][j])
        print_optimal_order(split, split[i][j] + 1, j)
        print(")", end="")


dims = [30, 35, 15, 5, 10, 20, 25]

# Example usage
dims = [30, 35, 15, 5, 10, 20, 25]  # Example matrix dimensions
min_cost, split = matrix_chain_multiplication(dims)
print("Minimum number of multiplications:", min_cost)
print("Optimal order of multiplication:")
print_optimal_order(split, 1, len(dims) - 1)
