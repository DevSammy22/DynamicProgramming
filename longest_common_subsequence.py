#totally mine
def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)
    opt = [[0] * (m + 1) for _ in range(n + 1)]
    b = [[""] * (m + 1) for _ in range(n + 1)]

    for i in range(1, (n + 1)):
        for j in range(1, (m + 1)):
            if A[i - 1] == B[j - 1]:
                opt[i][j] = opt[i - 1][j - 1] + 1
                b[i][j] = "diagonal"

            elif opt[i][j - 1] >= opt[i - 1][j]:
                opt[i][j] = opt[i][j - 1]
                b[i][j] = "left"

            else:
                opt[i][j] = opt[i - 1][j]
                b[i][j] = "up"

    return opt, b

def recover_optimal_solution(A, B, b):
    n = len(A)
    m = len(B)
    i = n
    j = m
    selected_strings = []
    while i > 0 and j > 0:
        if b[i][j] == "diagonal":
            selected_strings.append(A[i - 1])
            i = i - 1
            j = j - 1

        elif b[i][j] == "left":
            j = j - 1

        else:
            i = i - 1

    selected_strings.reverse()

    return "".join(selected_strings)

def lcs_solution(A, B):
    opt, b = longest_common_subsequence(A, B)
    lcs_character = recover_optimal_solution(A, B, b)
    lcs_length = opt[len(A)][len(B)]

    return lcs_character, lcs_length


# Example usage
A = "ABCBDAB"
B = "BDCAB"
lcs_character, lcs_length = lcs_solution(A, B)
print("LCS length:", lcs_length)
print("LCS character:", lcs_character)