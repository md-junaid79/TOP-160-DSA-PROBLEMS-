def maxSubArraySum(self, arr):
        # Your code here
        max_sum=float('-inf')  #or zero
        curr_sum=0
        
        for num in arr:
            #deciding whether to include the num or start a new subarray with num
            curr_sum=max(num,curr_sum+num)
            #updating max_sum if curr_sum is greater than max_sum
            max_sum=max(max_sum,curr_sum)
        return max_sum