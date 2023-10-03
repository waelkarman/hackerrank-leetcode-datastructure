
def reverse(llist):
    # Write your code here
    sol=[]
    sol.append(llist.data)
    while llist.next is not None:
        llist=llist.next
        sol.append(llist.data)
        
    sol.reverse()
    #print(sol)
    l=SinglyLinkedList()
    for a in sol:
        l.insert_node(a)
        #print(a)
    return l.head


