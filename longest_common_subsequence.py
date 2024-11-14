def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)

    # Step 1: Initialize the opt and pi tables with zeros
    opt = [[0] * (m + 1) for _ in range(n + 1)]
    pi = [[''] * (m + 1) for _ in range(n + 1)]  # To store directions

    # Step 2: Fill the opt table according to the pseudocode
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:  # Match found
                opt[i][j] = opt[i - 1][j - 1] + 1
                pi[i][j] = "diag"  # Diagonal arrow meaning we took a match
            elif opt[i][j - 1] >= opt[i - 1][j]:  # Left is better or equal
                opt[i][j] = opt[i][j - 1]
                pi[i][j] = "left"  # Left arrow meaning we skipped an element in B
            else:  # Top is better
                opt[i][j] = opt[i - 1][j]
                pi[i][j] = "up"  # Up arrow meaning we skipped an element in A

    # Step 3: Recover the LCS from the pi table
    def recover_LCS():
        lcs = []
        i, j = n, m
        while i > 0 and j > 0:
            if pi[i][j] == "diag":  # Diagonal: part of the LCS
                lcs.append(A[i - 1])
                i -= 1
                j -= 1
            elif pi[i][j] == "left":  # Move left
                j -= 1
            else:  # Move up
                i -= 1
        return ''.join(reversed(lcs))  # Reversing because we built it backwards

    # Step 4: Get the LCS length and sequence
    lcs_length = opt[n][m]
    lcs_sequence = recover_LCS()

    return lcs_length, lcs_sequence

# Example usage
A = "ABCBDAB"
B = "BDCAB"
lcs_length, lcs_sequence = longest_common_subsequence(A, B)
print("LCS Length:", lcs_length)
print("LCS Sequence:", lcs_sequence)
