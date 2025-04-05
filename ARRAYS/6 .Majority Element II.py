def findMajority(self, arr):
    
    l=len(arr)
    maj=l//3
    res=[]
    count={} #dictionary to store the freq of elements
    
    #counting the freq of elements
    for i in arr:
        if i not in count.keys():
            count[i]=1
        else:
            count[i]+=1
    
    #majority element finding logic
    #if freq of element is greater than l/3 then append it to res
    for key in (count.keys()):
        if count[key]>maj:
            res.append(key)
    
    #return sorted res as per question
    return sorted(res)