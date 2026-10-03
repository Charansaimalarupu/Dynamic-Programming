def climbing_stairs(n):
    if(n<=2):
        return n
    return climbing_stairs(n-1) + climbing_stairs(n-2)
def climbing_stairs_mem(n, dp):
    if(dp[n] != -1):
        return dp[n]
    if(n <= 2):
        return n
    dp[n] = climbing_stairs_mem(n-1, dp) + climbing_stairs_mem(n-2, dp)
    return dp[n]
def climbing_stairs_tab(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

dp = [-1] * 100  # Assuming a maximum value of 100 for n
print(climbing_stairs_mem(5, dp))  # Output: 8
print(climbing_stairs_tab(5))  # Output: 8  