def kthElement(a, b, k):
    n, m = len(a), len(b)
    
    # last element added to the merged sorted array
    last = 0
    i, j = 0, 0

    for _ in range(k):
        if i < n:
            # If a[i] > b[j] then increment j
            if j < m and a[i] > b[j]:
                last = b[j]
                j += 1
            # Otherwise increment i
            else:
                last = a[i]
                i += 1
        
        # If reached end of first array then increment j
        elif j < m:
            last = b[j]
            j += 1

    # Return the last (kth) element
    return last
