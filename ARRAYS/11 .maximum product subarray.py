def maxprodsubarray(self,arr):
    n = len(arr)

    # max&min product ending at the current index
    currMax = arr[0]
    currMin = arr[0]
    # Initialize overall max product
    maxProd = arr[0]

    # Iterate through the array
    for i in range(1, n):

        # Temporary variable to store the maximum product ending
        # at the current index
        temp = max(arr[i], arr[i] * currMax, arr[i] * currMin)

        # Update the minimum product ending at the current index
        currMin = min(arr[i], arr[i] * currMax, arr[i] * currMin)

        # Update the maximum product ending at the current index
        currMax = temp

        # Update the overall maximum product
        maxProd = max(maxProd, currMax)

    return maxProd