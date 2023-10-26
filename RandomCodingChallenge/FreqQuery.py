#USING AN ORDERED DATA STRUCTURE COULD SHRINK THE COMPLEXITY OF THE CASE 3
def freqQuery(queries):
    l={}
    a=[]
    for q in queries:
        if q[0] == 1:
            if q[1] not in l:
                l[q[1]]=1
            else:
                l[q[1]]+=1

        if q[0] == 2:
            if q[1] in l:
                if l[q[1]]>1:
                    l[q[1]]-=1
                else:
                    del l[q[1]]
        
        if q[0] == 3:
            a.append(0)
            for i in l:
                if l[i] == q[1]:
                    a.pop()
                    a.append(1)
                    