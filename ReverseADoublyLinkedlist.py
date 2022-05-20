
def reverse(llist):
    # Write your code here
    head = llist
    while llist is not None:
        tmp = llist.next
        llist.next = llist.prev
        llist.prev = tmp
        llist0=llist
        llist = llist.prev
    return llist0
        
