def stones(n, a, b):
    # Write your code here

    l=[0]
    ll=[]
    init=0
    for i in range(n-1):
        old_len=len(l)
        ll.clear()
        for e in range(init,len(l)):
            if l[e]+a not in ll:
                ll.append(l[e]+a)
            if l[e]+b not in ll:
                ll.append(l[e]+b)
        l=l+ll
        init=old_len

    ll.sort()
    return ll
    