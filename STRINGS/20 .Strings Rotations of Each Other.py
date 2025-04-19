class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #concat the string s1 with itself
        #if s2 is present in the concatenated string then s1 and s2 are rotations of each other
        concat=s1+s1
        return s2 in concat
        
