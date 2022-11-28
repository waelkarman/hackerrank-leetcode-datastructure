

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

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    if(position == 0):
        head = SinglyLinkedListNode(data)
        head.next = llist
        return head
    else:
        head = llist
        old_llist = llist
        count = 0
        while(llist is not None):
            if(position == count):
                new_node = SinglyLinkedListNode(data)
                old_llist.next = new_node
                new_node.next = llist
                break
            old_llist = llist
            llist = llist.next
            count += 1
        return head
