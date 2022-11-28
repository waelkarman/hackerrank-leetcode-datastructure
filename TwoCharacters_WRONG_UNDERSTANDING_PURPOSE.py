#finds longest alternating sequence
def alternate(s):
    # Write your code here
    max_count = 0 
    
    for index in range(len(s)):
        switch = True
        for k in range(index+1,len(s)):
            if s[k] == s[index]:
                continue
            count = 1
            l = []
            l.append(s[index])
            for i in range(k,len(s)): 
                if s[i] == s[k] and switch:
                    count+=1
                    l.append(s[k])
                    switch = False
                
                if s[i] == s[index] and not switch:
                    count+=1
                    l.append(s[index])
                    switch = True
            
            if count > max_count:
                max_count = count
            print(l,max_count)
    return max_count
