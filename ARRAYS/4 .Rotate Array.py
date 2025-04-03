def rotateArr(self, arr, d):

        l=len(arr)
        
        #if arr size is 1 then return it 
        if l==1:
            return arr
            
        #if d is large than size of array make it smaller
        d=d%l
        
        #slicing the array
        #concatenate (from d to end + from start to d ) 
        arr[:]=arr[d:]+arr[:d]
        
        return arr