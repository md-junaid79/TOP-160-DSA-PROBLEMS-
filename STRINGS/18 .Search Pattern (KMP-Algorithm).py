class Solution:
    def constructLps(self,pat, lps):
    
    # len stores the length of longest prefix which 
    # is also a suffix for the previous index
        len_ = 0
        m = len(pat)
        
        # lps[0] is always 0
        lps[0] = 0
    
        i = 1
        while i < m:
            
            # If characters match, increment the size of lps
            if pat[i] == pat[len_]:
                len_ += 1
                lps[i] = len_
                i += 1
            
            # If there is a mismatch
            else:
                if len_ != 0:
                    
                    # Update len to the previous lps value 
                    # to avoid redundant comparisons
                    len_ = lps[len_ - 1]
                else:
                    
                    # If no matching prefix found, set lps[i] to 0
                    lps[i] = 0
                    i += 1

    def search(self,pat, txt):
        n = len(txt)
        m = len(pat)
    
        lps = [0] * m
        res = []
    
        self.constructLps(pat, lps)
    
        # Pointers i and j, for traversing 
        # the text and pattern
        i = 0
        j = 0
    
        while i < n:
            
            # If characters match, move both pointers forward
            if txt[i] == pat[j]:
                i += 1
                j += 1
    
                # If the entire pattern is matched 
                # store the start index in result
                if j == m:
                    res.append(i - j)
                    
                    # Use LPS of previous index to 
                    # skip unnecessary comparisons
                    j = lps[j - 1]
            
            # If there is a mismatch
            else:
                
                # Use lps value of previous index
                # to avoid redundant comparisons
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return res
    
        

        
# Example usage
s = Solution()
txt = "ababcabcabababd"
pat = "ababd"   
result = s.search(pat, txt)
print(result)  # Output: [10]