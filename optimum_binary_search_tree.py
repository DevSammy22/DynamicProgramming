#mine
import sys
def optimum_binary_search_tree(frequencies):
    n = len(frequencies)
    fsum = [0] * (n + 1)
    for i in range(1, (n + 1)):
        fsum[i] = fsum[i - 1] + frequencies[i - 1]

    opt = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    for length in range(1, (n + 1)):
        for i in range(n - length + 1):
            j = i + length - 1
            #opt[i][j] = float("inf")
            opt[i][j] = sys.maxsize
            for k in range(i, (j + 1)):
                left_cost = opt[i][k - 1] if k > i else 0
                right_cost = opt[k + 1][j] if k < j else 0
                total_cost = left_cost + right_cost
                if total_cost < opt[i][j]:
                    opt[i][j] = total_cost
                    root[i][j] = k

            opt[i][j] = opt[i][j] + fsum[j + 1] - fsum[i]

    return opt, root


def print_tree(root, i, j):

    if i > j:
        return
    else:
        k = root[i][j]
        print("(", end=" ")
        print_tree(root, i, k - 1)
        print(f" {k}", end=" ")
        print_tree(root, k + 1, j)
        print(")", end=" ")

# Frequencies of searches for nodes
frequencies = [0.1, 0.2, 0.4, 0.3]

optimal_cost, root = optimum_binary_search_tree(frequencies)

print("The tree structure is: ")
print_tree(root, 0, len(frequencies) - 1)

