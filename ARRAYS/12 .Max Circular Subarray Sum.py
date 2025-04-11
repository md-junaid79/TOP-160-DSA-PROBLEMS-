def circularSubarraySum(arr):
    def kadane(nums):
        # Find the maximum subarray sum using Kadane's algorithm
        maxsum = float('-inf')
        currsum = 0
        for num in nums:
            currsum = max(num, num + currsum)
            maxsum = max(maxsum, currsum)
        return maxsum

    # Maximum subarray sum for the original array
    maxsum = kadane(arr)
    # Minimum subarray sum by negating the array
    minsum = kadane([-i for i in arr])
    # Total sum of the array
    totsum = sum(arr)

    # If all elements are negative, return maxsum
    if maxsum < 0:
        return maxsum
    # Return the maximum of non-circular and circular subarray sums
    return max(maxsum, totsum + minsum)