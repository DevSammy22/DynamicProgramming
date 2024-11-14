def subset_sum(weights, target_sum):
    n = len(weights)  # Number of items

    # Initialize the opt and b tables
    # opt[i][W'] will be True if we can achieve the sum W' using the first i items, otherwise False
    opt = [[False] * (target_sum + 1) for _ in range(n + 1)]
    # b[i][W'] will help us remember if we included the i-th item to achieve the sum W'
    b = [['N'] * (target_sum + 1) for _ in range(n + 1)]

    # Base case: A sum of 0 can always be achieved by including no items
    for i in range(n + 1):
        opt[i][0] = True

    # Fill the opt and b tables
    for i in range(1, n + 1):  # Loop through items
        for W in range(target_sum + 1):  # Loop through all possible sums up to target_sum
            # Option 1: Exclude the current item
            opt[i][W] = opt[i - 1][W]
            b[i][W] = 'N'

            # Option 2: Include the current item if it fits in the current sum W
            if weights[i - 1] <= W and opt[i - 1][W - weights[i - 1]]:
                opt[i][W] = True
                b[i][W] = 'Y'

    # Return the final result (True or False) and the table for backtracking
    return opt[n][target_sum], b


def recover_solution(b, weights, target_sum):
    # This function reconstructs the subset that adds up to target_sum
    solution = []
    weight_indices = []
    i = len(weights)
    W = target_sum

    # Trace back from b table to find which items were included
    while i > 0 and W > 0:
        if b[i][W] == 'Y':  # If item i was included
            solution.append(weights[i - 1])  # Add this item to the solution
            weight_indices.append(i - 1)
            W -= weights[i - 1]  # Decrease the sum by the item's weight
        i -= 1  # Move to the previous item

    # Return the items in the order they were added
    return solution[::-1], weight_indices[::-1]


def subset_sum_result(weights, target_sum):
    # Check if the subset sum is possible and retrieve the subset if it exists
    is_possible, b = subset_sum(weights, target_sum)

    if is_possible:
        chosen_items, weights_inx = recover_solution(b, weights, target_sum)
    else:
        chosen_items = []

    return is_possible, chosen_items, weights_inx


# Example usage
weights = [3, 34, 4, 12, 5, 2, 8, 9, 4, 20]
target_sum = 15
is_possible, chosen_items, weights_inx = subset_sum_result(weights, target_sum)

print("Is target sum achievable?", is_possible)
print("Subset of weights that sum to target:", chosen_items)
print("index:", weights_inx)
