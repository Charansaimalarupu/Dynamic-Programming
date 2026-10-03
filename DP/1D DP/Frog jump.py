def frog_jump(heights,n):
    if(n==0):
        return 0
    left=frog_jump(heights,n-1)+abs(heights[n]-heights[n-1])
    right=float('inf')
    if(n>1):
        right=frog_jump(heights,n-2)+abs(heights[n]-heights[n-2])

    return min(left,right)
def frog_jump_mem(heights,n,dp):
    if(n==0):
        return 0
    if(dp[n]!=-1):
        return dp[n]
    left=frog_jump_mem(heights,n-1,dp)+abs(heights[n]-heights[n-1])
    right=float('inf')
    if(n>1):
        right=frog_jump_mem(heights,n-2,dp)+abs(heights[n]-heights[n-2])
    dp[n]=min(left,right)
    return dp[n]
def frog_jump_tab(heights,n):
    dp=[-1]*(n+1)
    dp[0]=0
    dp[1]=abs(heights[1]-heights[0])
    for i in range(2,n+1):  
        left=dp[i-1]+abs(heights[i]-heights[i-1])
        right=dp[i-2]+abs(heights[i]-heights[i-2])
        dp[i]=min(left,right)
    return dp[n]    
heights=[30,20,50,10,40]
print(frog_jump(heights,4)) #Output: 40
print(frog_jump_mem(heights,4,[-1]*5)) #Output: 40
print(frog_jump_tab(heights,4)) #Output: 40
