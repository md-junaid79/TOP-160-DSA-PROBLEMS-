def getMinDiff(self, arr,k):
        n = len(arr)
        arr.sort()
        big=arr[-1]
        small=arr[0]
        #initial result after sorting
        res = big - small

        for i in range(1, len(arr)):
            # Impossible to decrement height of ith tower by k, 
            # continue to the next tower
            if arr[i] - k < 0:
                continue
            # For all indices i, increment arr[0...i-1] by k and
            # decrement arr[i...n-1] by k
            minH = min(small + k, arr[i] - k)
    
            maxH = max(big - k,arr[i - 1] + k)
    
            res = min(res, maxH - minH)
        return res