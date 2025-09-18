class Solution:
    def mergeOverlap(self, arr):
        #Code 
        arr.sort()
        res = []
        res.append(arr[0])
        if len(arr)==1:
            return arr
        for i in range(1,len(arr)):
            last = res[-1]
            curr = arr[i]
            if curr[0] <= last[1]:
                last[1] = max(last[1],curr[1])
            else:
                res.append(curr)
        return res
		
# Example usage:
if __name__ == "__main__":
    arr = [[1, 3], [2, 4], [5, 7], [6, 8]]
    sol = Solution()
    print(sol.mergeOverlap(arr))  # Output: [[1, 4], [5, 8]]