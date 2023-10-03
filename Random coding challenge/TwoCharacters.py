# right implementation
def alternate(s):
    # Write your code here
    max_count = 0 
    history = []
    for index in range(len(s)):
        switch = True
        for k in range(index+1,len(s)):
            if s[k] == s[index]:
                continue
            if history.count((s[k],s[index]))>0 or history.count((s[index],s[k]))>0  :
                continue
            else:
                history.append((s[k],s[index]))
            ss=s
            for i in s:
                if i != s[k] and i != s[index]:
                    ss = ss.replace(i,"")
            
            #check if ss is alterante
            jump = False
            switch = False
            if ss[0] == s[k]:
                switch = True
            for c in ss:
                if(s[k] == c and switch):
                    switch = False                    
                    continue
                if(s[index] == c and not switch):
                    switch = True
                    continue
                jump = True
            if jump:
                continue
            
            #save max_count
            if len(ss)>max_count:
                max_count = len(ss)
            
    return max_count




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
