class Solution:
    def findMin(self, arr):
        l=len(arr)
        if l==1:
            return arr[0]
        else:
            hi=l-1
            lo=0
            
            while lo<hi:
                mid=(lo+hi)//2
                
                if arr[lo]<arr[hi]:
                    return arr[lo]
                
                if arr[mid]>arr[hi]:
                    lo=mid+1
                
                else:
                    hi=mid
            return arr[lo]
                    
                    
