def addBinary(self, s1, s2):
    # Remove leading zeroes
    s1 = s1.lstrip("0")
    s2 = s2.lstrip("0")
    
    # Get lengths of both strings
    l1 = len(s1)
    l2 = len(s2)
    
    # Ensure s1 is the longer string
    if l2 > l1:
        s1, s2 = s2, s1
        l1, l2 = l2, l1
    
    # Initialize pointers and variables
    j = l2 - 1  # Pointer for the shorter string (s2)
    carry = 0   # Carry for addition
    result = [] # List to store the binary result
    
    # Loop through s1 from the end
    for i in range(l1 - 1, -1, -1):
        bit1 = int(s1[i])  # Current bit of s1
        bitSum = bit1 + carry
        
        # Add corresponding bit from s2 if within bounds
        if j >= 0:
            bit2 = int(s2[j])
            bitSum += bit2
            j -= 1
        
        # Compute the current bit and carry
        bit = bitSum % 2
        carry = bitSum // 2
        
        # Append the current bit to the result
        result.append(str(bit))
    
    # If there's a carry left, append it
    if carry > 0:
        result.append("1")
    
    # Reverse the result and join to form the final binary string
    return ''.join(result[::-1])




