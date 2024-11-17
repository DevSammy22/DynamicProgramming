def knapsack(n, prices, budget, values):
    DP = [0] * (budget + 1)
    choice = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, (n + 1)):
        if i <= n//2:
            for j in range(prices[i - 1], (budget + 1)):
                if DP[j] < DP[j - prices[i - 1]] + values[i - 1]:
                    DP[j] = DP[j - prices[i - 1]] + values[i - 1]
                    choice[i][j] = 1

        else:
            for j in range(budget, prices[i - 1] - 1, -1):
                if DP[j] < DP[j - prices[i - 1]] + values[i - 1]:
                    DP[j] = DP[j - prices[i - 1]] + values[i - 1]
                    choice[i][j] = 1

    return DP, choice

def recovery_solution(n, prices, budget, values, choice, DP):
    selected_value = [0] * n

    for i in range(n, 0, -1):
        if choice[i][budget] == 1:
            if i <= n//2: #unlimimted copy
                while budget >= prices[i - 1] and choice[i][budget] == 1:
                    selected_value[i - 1] += 1
                    budget -= prices[i - 1]

            else: #only one copy
                selected_value[i - 1] = 1
                budget -= prices[i - 1]

    selected_value.reverse()
    return selected_value

def result(n, prices, budget, values):
    DP, choice = knapsack(n, prices, budget, values)
    maximum_value = DP[budget]
    selected_items = recovery_solution(n, prices, budget, values, choice, DP)

    return maximum_value, selected_items

n = 4  # Number of items
values = [6, 10, 12, 8]  # Values of the items
prices = [3, 4, 5, 6]  # Prices of the items
budget = 10
maximum_value, selected_value = result(n, prices, budget, values)

print("Maximum value: ", maximum_value)
print("Selected values: ", selected_value)






