def isMatch(s, p):
    m, n = len(s), len(p)
    #print(m,n)

    # Create a DP table initialized with False
    dp = []
    for i in range(m+1):
        row=[]
        for j in range(n+1):
            row.append(False)
        dp.append(row)
    #print(dp)

    dp[0][0] = True

    # Fill in the first row
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill in the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]


# Example
s = "cb"
p = "?b"
print(isMatch(s, p))
