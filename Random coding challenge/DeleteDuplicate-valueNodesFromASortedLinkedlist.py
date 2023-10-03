

def removeDuplicates(llist):
    # Write your code here
    head = llist
    head0 = llist
    data = llist.data
    if llist.next is not None:
        llist = llist.next
    while llist is not None:
        if llist.data == data :
            head0.next = llist.next
            #remove it
            pass
            llist = llist.next
        else:
            head0 = llist
            data = llist.data
            llist = llist.next
    
    return head

