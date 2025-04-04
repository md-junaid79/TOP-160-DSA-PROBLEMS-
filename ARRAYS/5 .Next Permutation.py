def nextPermutation(arr):

        l=len(arr)
        pivot=-1
        for i in range(l-2,-1,-1):
            if arr[i]<arr[i+1]:
                pivot=i
                break
        if pivot==-1:
            return arr[::-1]
        
        #swap with right most greater element
        
        for i in range(l-1,pivot,-1):
            if arr[i]>arr[pivot]:
                arr[i],arr[pivot]=arr[pivot],arr[i]
                break
                
        # reverse the remaining array
        
        return arr[:pivot+1]+arr[:pivot:-1]
        # or we can also return arr by this -> arr[pivot+1:]=reversed(arr[pivot+1:])
    
arr = [2, 4, 1, 7, 5, 0]
arr2=[1,3,2]
print(nextPermutation(arr2))