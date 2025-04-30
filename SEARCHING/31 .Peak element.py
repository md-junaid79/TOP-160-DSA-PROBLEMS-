
def peakElement(self,arr):
    # Code here
    l=len(arr)
    
    
    if l==1:
        return 0
        
    if arr[0]>arr[1]:
        return 0
    
    if arr[l-1]>arr[l-2]:
        return (l-1)
        
        
    lo=1
    hi=l-2
    while lo<=hi:
        mid=(lo+hi)//2
        
        if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
            return mid
        if arr[mid]<arr[mid+1]:
            lo=mid+1
            
        else:
            hi=mid-1
        
