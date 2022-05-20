

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    head = llist
   
    while llist is not None:
        if position > 0:
            if llist.next is not None:     
                position-=1
                list0=llist
                llist=llist.next
            else:
                return head 
        else:
            a = SinglyLinkedListNode(data)
            list0.next = a
            a.next = llist
            return head
        
    return head


