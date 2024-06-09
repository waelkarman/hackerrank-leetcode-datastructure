def luckBalance(k, contests):
    # Write your code here
    total = 0
    l=[]
    for i in contests:
        total += i[0]
        if i[1] == 1:
            l.append(i[0])
    l.sort()
    towin=len(l)-k
    for j in range(towin):
        total-=l[j]*2
        
    return total
