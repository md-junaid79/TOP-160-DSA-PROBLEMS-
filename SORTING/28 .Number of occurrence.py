class Solution:
    def countFreq(self, arr, target):
        #code here
        f=arr.count(target)
        return f
#----OR----
#use binary search to find the first and last occurrence of the target element in the array.

def lowerbound(arr, target):
    res=len(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + (high-low)) // 2
        if arr[mid] >= target:
            res=mid
            high = mid - 1
            
        else:
            low = mid + 1
    return res

def higherbound(arr, target):
    res=len(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + (high-low)) // 2
        if arr[mid] > target:
            res=mid
            high = mid - 1
            
        else:
            low = mid + 1
    return res

def countFreq(arr, target):
    first = lowerbound(arr, target)
    last = higherbound(arr, target)
    return last - first 

#example usage
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
ans=countFreq(arr, target)                  # Output: 3
print(ans)