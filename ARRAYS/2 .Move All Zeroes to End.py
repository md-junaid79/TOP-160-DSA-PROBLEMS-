def pushZerosToEnd(self,arr):
    c=0   #keep track of non-zero elements
    
    for i in range(len(arr)):
        #if nonzero element is found, swap it with the first zero element
        if arr[i]!=0:
            arr[i],arr[c]=arr[c],arr[i]
            c+=1
    return arr