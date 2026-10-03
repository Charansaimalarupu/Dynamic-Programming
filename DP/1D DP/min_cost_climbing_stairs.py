def mincost(cost,n):
    if(n==0):
        return cost[0]
    if(n==1):
        return cost[1]
    left=mincost(cost,n-1)+cost[n-1]
    right=float('inf')
    if(n>1):
        right=mincost(cost,n-2)+cost[n-2]
    return min(left,right)
print(mincost([10,15,20],3)) #Output: 15