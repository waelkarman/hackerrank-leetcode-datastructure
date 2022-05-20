
def insertNodeAtTail(head, data):
    if head is None:
        a=SinglyLinkedListNode(data)
        return a
        
    
    first = head
    while head.next is not None:
        head = head.next
    a=SinglyLinkedListNode(data)
    head.next=a
    
    return first
    

