#totally mine
def edit_distance(str_1, str_2):
    n = len(str_1)
    m = len(str_2)

    opt = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        opt[i][0] = i
        for j in range(m):
            opt[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str_1[i - 1] == str_2[j - 1]:
                opt[i][j] = opt[i - 1][j - 1]
            else:
                opt[i][j] = 1 + min(
                                    opt[i - 1][j - 1], # replacement
                                    opt[i][j - 1], # insertion
                                    opt[i - 1][j] # deletion
                                    )
    edit_distance_length = opt[n][m]

    return edit_distance_length, opt

def recover_optimal_solution(str_1, str_2, opt):
    i = len(str_1)
    j = len(str_2)
    solution = []

    while i > 0 and j > 0:
        if i > 0 and j > 0 and str_1[i - 1] == str_2[j - 1]:
            # No operation needed
            i = i - 1
            j = j - 1

        elif i > 0 and j > 0 and opt[i][j] == opt[i - 1][j - 1] + 1:
            # Replacement operation
            solution.append(f"Replace letter '{str_1[ i - 1]}' in S1 with letter '{str_2[j - 1]}' at position {i}")
            i = i - 1
            j = j - 1

        elif i > 0 and opt[i][j] == opt[i - 1][j] + 1:
            # Deletion operation
            solution.append(f"Delete letter '{str_1[i - 1]}' in S1 at position {i}")
            i = i - 1

        elif j > 0 and opt[i][j] == opt[i][j - 1] + 1:
            # Insertion operation
            solution.append(f"Insert letter '{str_2[j - 1]}' into S1 at position {i + 1}")
            j = j - 1

    solution.reverse()

    return solution


def solution(str_1, str_2):

    edit_distance_length, opt = edit_distance(str_1, str_2)
    steps_to_edit = recover_optimal_solution(str_1, str_2, opt)

    return edit_distance_length, steps_to_edit





# Example usage
s1 = "intention"
s2 = "execution"
number_of_operation, opt = edit_distance(s1, s2)
recover_solution = recover_optimal_solution(s1, s2, opt)
print("The number of operation is: ", number_of_operation)
for step in recover_solution:
    print(step)


