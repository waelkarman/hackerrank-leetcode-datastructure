
def alternatingCharacters(s):
    # Write your code here
    n = 0
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            n += 1
    
    return n 

