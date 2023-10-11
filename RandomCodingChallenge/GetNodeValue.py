

def getNode(llist, positionFromTail):
    # Write your code here
    sol=[]
    sol.append(llist.data)
    while llist.next is not None:
        llist=llist.next
        sol.append(llist.data)
        
    sol.reverse()
    return sol[positionFromTail]
    #print(sol)
    #for a in sol:
    #    print(a)


