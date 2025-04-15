def areAnagrams(self, s1, s2):
    #code here
    
    return sorted(s1)==sorted(s2)


    #other approach with dictionary
        # if lengths are different, can't be anagrams
        # if len(s1)!=len(s2):
        #     return False
        # d1 = {}
        # # count frequency of chars in s1
        # for i in s1:
        #     d1[i] = d1.get(i, 0) + 1
        # # check if chars in s2 match s1
        # for i in s2:
        #     if i not in d1:
        #         return False
        #     d1[i] -= 1
        #     # remove char if count becomes 0
        #     if d1[i] == 0:
        #         del d1[i]
        # # if dictionary is empty, strings are anagrams
        # return len(d1) == 0    