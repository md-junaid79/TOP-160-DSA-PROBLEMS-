def getSecondLargest(self, arr):
        
        #initialize 2 variables : largest and second largest
        lar=-1
        slar=-1
        for i in arr:
            ## check if current element is greater than largest
            if i>lar:
                slar=lar
                lar=i
            # check if current element is smaller than largest but greater than second largest
            elif i<lar and slar<i:
                slar=i
            # if it is equal to largest, we do not do anything
            else:
                continue
        return slar