print("hellow")


def fib(n):
    if(n<=1):
        return n
    return fib(n-1) + fib(n-2)


def fib_mem(n,dp1):
    if (dp1[n]!=-1):
        return dp1[n]
    if(n<=1):
        return n
    dp1[n] = fib_mem(n-1,dp1) + fib_mem(n-2,dp1)
    return dp1[n]

dp1 = [-1] * 100  # Assuming a maximum value of 100 for n
print(fib_mem(7, dp1))  # Output: 8

#tabulation
def fib_tab(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(fib_tab(7))  # Output: 8
