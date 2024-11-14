#totally mine
def knapsack(weights, values, max_weight):
    n = len(weights)
    opt = [[0] * (max_weight + 1) for _ in range(n + 1)]
    b = [["N"] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, (n+1)):
        for W in range(max_weight + 1):
            opt[i][W] = opt[i - 1][W]
            b[i][W] = "N"
            if weights[i - 1] <= W and (opt[i - 1][W - weights[i - 1]] + values[i - 1]) >= opt[i][W]:
                opt[i][W] = opt[i - 1][W - weights[i - 1]] + values[i - 1]
                b[i][W] = "Y"

    return opt, b

def recover_optimal_solution(weights, max_weight, b):
    i = len(weights)
    selected_item = []

    while i > 0:
        if b[i][max_weight] == "Y":
            selected_item.append(i - 1)
            max_weight = max_weight - weights[i - 1]

        i = i - 1

    selected_item.reverse()

    return selected_item

def result(weights, values, max_weight):

    opt, b = knapsack(weights, values, max_weight)
    maximum_value = opt[len(weights)][max_weight]
    selected_items = recover_optimal_solution(weights, max_weight, b)

    return maximum_value, selected_items
# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
max_weight = 5

max_value, recover_solution = result(weights, values, max_weight)
print("Maximum value: ", max_value)
print("recover solution: ", recover_solution)



