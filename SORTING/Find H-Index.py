#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        
        #OPTIMAL APPROACH TC:O(N) 
        n=len(citations)
        # Array to store frequency of citations
        freq=[0]*(n+1)
        
        # Count frequencies of citations
        for i in citations:
            if i>=n:
                freq[n]+=1
            else:
                freq[i]+=1
        
        i=n
        s=freq[n]
        # Find largest i where at least i papers have i citations
        while s<i:
            i-=1
            s+=freq[i]
        return i
        
        #another approach TC:O(Nlogn)
        
        # citations.sort(reverse=True)
        # n=len(citations)
        # i=0
        
        # while i<n and citations[i]>=i :
        #     i+=1
        # return i
            
