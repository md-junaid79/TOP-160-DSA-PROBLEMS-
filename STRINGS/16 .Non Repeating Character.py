class Solution:
    def nonRepeatingChar(self,s):
        #using hashing by creating a dictionary
        dict={}
        
        #treverse and get all element's frequencies
        for i in s:
            if i not in dict.keys():
                dict[i]=1
            else:
                dict[i]+=1
        #traverse the dictkeys where their freq is 1.return it 
        for num in dict.keys():
            if dict[num]==1:
                return num
        #else return  or -1 as per requirement   
        return "$"
            
s="geeksforgeeks"
solution = Solution()
result = solution.nonRepeatingChar(s)
print(result)       
    

