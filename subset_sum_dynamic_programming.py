#totally mine
def knapsack(weights, max_weight):
    n = len(weights)
    opt = [[False] * (max_weight + 1) for _ in range(n + 1)]
    b = [["N"] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        opt[0][0] = True

    for i in range(1, (n+1)):
        for W in range(max_weight + 1):
            opt[i][W] = opt[i - 1][W]
            b[i][W] = "N"
            if weights[i - 1] <= W and (opt[i - 1][W - weights[i - 1]] + weights[i - 1]) >= opt[i][W]:
                opt[i][W] = True
                b[i][W] = "Y"

    return opt, b

def recover_optimal_solution(weights, max_weight, b):
    i = len(weights)
    selected_item = []
    selected_item_weight = []

    while i > 0:
        if b[i][max_weight] == "Y":
            selected_item.append(i - 1)
            selected_item_weight.append(weights[i - 1])
            max_weight = max_weight - weights[i - 1]

        i = i - 1

    selected_item.reverse()
    selected_item_weight.reverse()

    return selected_item, selected_item_weight

def result(weights, max_weight):

    opt, b = knapsack(weights, max_weight)
    isSelected = opt[len(weights)][max_weight]
    if isSelected:
        selected_items, selected_items_weight = recover_optimal_solution(weights, max_weight, b)
    else:
        selected_items, selected_items_weight = [], []

    return isSelected, selected_items, selected_items_weight
# Example usage
weights = [3, 34, 4, 12, 5, 2, 8, 9, 4, 20]
target_sum = 15

isSelected, selected_items_index, selected_items_weight = result(weights, target_sum)

print("Is possible to achieve max values with selected items?: ", isSelected)
print("Selected item index: ", selected_items_index)
print("Selected item weight: ", selected_items_weight)




