
def sortedInsert(llist, data):
    # Write your code here    
    head = llist

    if head is None:
        head = DoublyLinkedListNode(data)
    
    while llist is not None:
        #print(f"-----{llist.data} > {data}:")
        if llist.data < data:
            if llist.next is not None:
                llist=llist.next
            else:
                llist.next = DoublyLinkedListNode(data)
                return head
        else:
            if llist.prev is not None:
                a = DoublyLinkedListNode(data)
                a.prev = llist.prev
                a.next = llist
                llist.prev.next = a
                llist.prev = a                    
                return head
            else:
                a = DoublyLinkedListNode(data)
                a.next=llist
                head = a 
                return head               
                
    return head 
    
