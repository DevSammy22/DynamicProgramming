def longest_increasing_subsequnce(A):
    if not A:
        return 0, []

    n = len(A)
    opt = [1] * n
    previous = [-1] * n

    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and opt[j] + 1 > opt[i]:
                opt[i] = opt[j] + 1
                previous[i] = j

    max_value = max(opt)
    max_index = opt.index(max_value)

    lcs = []
    while max_index != -1:
        lcs.append(A[max_index])
        max_index = previous[max_index]
    lcs.reverse()
    return max_value, lcs


# Example usage
A = [10, 9, 2, 5, 3, 7, 101, 18]
lcs_max_value, lcs_length = longest_increasing_subsequnce(A)
print("Length of longest increasing subsequence: ", lcs_max_value)
print("Longest increasing subsequence: ", lcs_length)
