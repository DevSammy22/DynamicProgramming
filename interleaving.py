#totally mine
def interleaving(S1, S2, S3):
    n = len(S1)
    m = len(S2)
    if n + m < len(S3):
        return False

    opt = [[False] * (m + 1) for _ in range(n + 1)]
    opt[0][0] = True

    for i in range(1, n + 1):
        opt[i][0] = opt[i - 1][0] and S1[i - 1] == S3[i - 1]

    for j in range(1, m + 1):
        opt[0][j] = opt[0][j - 1] and S2[j - 1] == S3[j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S1[i - 1] == S3[i + j - 1]:
                opt[i][j] = opt[i - 1][j]

            if S2[j - 1] == S3[i + j - 1]:
                opt[i][j] = opt[i][j] or opt[i][j - 1]

    isInterleaving = opt[n][m]

    return isInterleaving



s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
isInterleaving = interleaving(s1, s2, s3)
print(isInterleaving)  # Output: True


