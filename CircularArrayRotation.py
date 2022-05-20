

def circularArrayRotation(a, k, queries):
    # Write your code here
    fin=[]
    for j in queries:
        if k>len(a):
            k=k%len(a)
        p=j-k
            
        fin.append(a[p])
    return fin
    
