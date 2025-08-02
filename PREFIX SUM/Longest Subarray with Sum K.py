def maxLen(arr,k):
    seen={}     #dictionary to store the sum and index
    seen[0]=-1   #to handle the case when subarray starts from index
    sum=0        
    maxlen=0
    
    for i,num in enumerate(arr):
        sum+=num
        
        if sum==k:
            maxlen=max(maxlen,i+1)    #maxlen is i+1 if sum equals k
        elif sum-k in seen:
            maxlen=max(maxlen,i-seen[sum-k])
        else:
            seen[sum]=i             #store the index of sum
    return maxlen
    
    
# Example usage:
arr=[94, -33, -13, 40, -82, 94, -33, -13, 40, -82]
k=52
print(maxLen(arr,k))  