

def merge(l):
    
    if len(l)>1:
            

        R = l[:len(l)//2]
        L = l[len(l)//2:]

        merge(R)
        merge(L)

        i=0
        j=0
        q=0
        while j < len(L) and i < len(R):
                if R[i]>L[j]:
                    l[q]=L[j]
                    j+=1
                    q+=1
                else:     
                    l[q]=R[i]
                    i+=1
                    q+=1
            
            
        while j < len(L):
            l[q] = L[j]
            j += 1
            q += 1
 
        while i < len(R):
            l[q] = R[i]
            i += 1
            q += 1

l=[4,5,7,2]
merge(l)
print(l)
