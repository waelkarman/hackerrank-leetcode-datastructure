def countSwaps(a):
    print(a)
    # Write your code here
    for i in range(len(a)):
        for j in range(len(a) - 1):
            # Swap adjacent elements if they are in decreasing order
            print(f"{a[j]} > {a[j + 1]}")
            if a[j] > a[j + 1]:
                #tmp=a[j]
                #a[j]=a[j+1]
                #a[j+1]=tmp
                a=swap(a,j,j + 1)
        
    print(a)
    return a
    
def swap(l,v,u):
    tmp=l[v]
    l[v]=l[u]
    l[u]=tmp
    return l


countSwaps([7,8,6])

