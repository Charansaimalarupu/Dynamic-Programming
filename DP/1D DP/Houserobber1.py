def house_robber (nums,n):
    if(n==0):
        return nums[0]
    if(n<0):
        return 0    
    return max(house_robber(nums,n-1),house_robber(nums,n-2)+nums[n])

def house_robber_mem(nums,n,dp):
    if(n==0):
            return nums[0]
    if(n<0):
        return 0    
    if(dp[n]!=-1):
        return dp[n]
    
    dp[n]= max(house_robber(nums,n-1),house_robber(nums,n-2)+nums[n])
    return dp[n]
def house_robber_tab(nums,n):
    dp=[0]*(n+1)
    dp[0]=nums[0]
    for i in range(1,n+1):
        dp[i]=max(dp[i-1],dp[i-2]+nums[i])
    return dp[n]        
print(house_robber([1,2,3,1],3)) #Output: 4
dp=[-1]*100

