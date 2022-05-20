

def repeatedString(s, n):
    # Write your code here
    num=0
    to = n%len(s)
    for i in range(to):
        if s[i] == 'a':
            num+=1
    return num+s.count('a')*int(n/len(s))    
        
