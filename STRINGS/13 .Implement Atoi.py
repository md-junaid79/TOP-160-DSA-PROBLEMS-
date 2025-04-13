def myAtoi(self, s):
    # REMOVING UNWANTED WHIITE SPACES 
    s=s.strip()
    if not s:
        return 0
    #SIGN BIT =1 AND THEN CHECKING FOR "-"
    sign=1
    i=0
    if s[0]=='+':
        i+=1
    elif s[0]=='-':
        sign=-1
        i+=1
        
    result=0
    # i means the position of sign bit,..
    #starting from "i" until we encounter any nondigit we exit the loop
    #res*=10+int(s[i])
    while i<len(s) and s[i].isdigit():
        result=result*10+int(s[i])
        i+=1
    result *=sign
    
    INT_MAX=2**31-1
    INT_MIN=-2**31
    if result>INT_MAX:
        return INT_MAX
    elif result<INT_MIN:
        return INT_MIN
    else:
        return result
#ALL TEST CASES PASSED..