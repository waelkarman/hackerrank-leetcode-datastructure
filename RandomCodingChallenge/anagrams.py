def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
         
    sol=0
    str1=s[0:int(len(s)/2)]
    str2=s[int(len(s)/2):len(s)]
    
    l1=list(str1)
    l2=list(str2)
    
    #print(f"{l1} -- {l2}")
    counter=0
    i=0
    
    while i < len(l1):
        j=0
        jump=True
        while j < len(l2):
            if l1[i] == l2[j]:
                counter+=1
                l1.pop(i)
                l2.pop(j)
                #print(f"{l1} -- {l2}")
                i=0
                jump=False
                continue
            j+=1
        if jump:
            i+=1

    return len(str1)-counter
