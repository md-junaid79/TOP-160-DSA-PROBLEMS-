def kthMissing( arr, k):
    # binary Search for index where  arr[i] > (i + k)
    n=len(arr)
    lo,hi=0,n-1
    res = n+k      # if arr has no missing values [1,2,3,4] 
    
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]>mid+k:
            res=mid+k        
            hi=mid-1        #search in the left half
        else:
            lo=mid+1        #search in the right half
    return res
            
        
                

arr = [1,2,3,4,6]
k = 2
print(kthMissing(arr, k))        