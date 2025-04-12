def missingNumber(self,arr):
    #for storing the array elements in a dict 
    mydict={}

    for i in arr:
        if i>0  :
            if i not in mydict.keys():
                mydict[i]=1
    j=1
    #for searching smallest +ve no. starting from 1
    while True:
        #if j is not present in the dict then return it
        #else increment j by 1 and check again
        if j not in mydict.keys():
            return j
        else:
            j+=1