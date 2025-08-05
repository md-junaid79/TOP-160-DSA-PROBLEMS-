def reverseArray(arr):
        
        #two pointer technique
        first=0
        last=len(arr)-1
        
        while first<last:
            # swap the elements
            arr[first],arr[last]=arr[last],arr[first]
            first+=1
            last-=1
        return arr
A=[1,2,3,4,5]
print(reverseArray(A))