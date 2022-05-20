
def compare_lists(llist1, llist2):
    i=0
    j=0
    sol1=[]
    sol2=[]
    while llist1.next is not None:
        llist1 = llist1.next
        sol1.append(llist1.data)
        i+=1
            
    while llist2.next is not None:
        llist2 = llist2.next
        sol2.append(llist2.data)
        j+=1
        
    if i==j and sol1==sol2:
        return 1
    else:
        return 0
    

