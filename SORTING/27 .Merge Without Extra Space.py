class Solution:
    
    def mergeArrays(self,a, b):
        i = len(a) - 1
        j = 0
    
        # Swap smaller elements from b[] with larger elements from a[]
        while i >= 0 and j < len(b):
            if a[i] < b[j]:
                i -= 1
            else:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
    
        # Sort both arrays
        a.sort()
        b.sort()
