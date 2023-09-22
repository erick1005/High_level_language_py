def paliPartitioning(s, k):
    n = len(s)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + (s[i] != s[j])
    
    dp2 = [float('inf') for _ in range(n+1)]
    dp2[0] = 0
    for i in range(1, n+1):
        for j in range(i):
            if s[j:i] == s[j:i][::-1]:
                dp2[i] = min(dp2[i], dp2[j] + 1)
    
    return dp2[n] <= k

s = input()
k = int(input())
print(paliPartitioning(s, k))