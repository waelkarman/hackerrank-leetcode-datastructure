
def mergeLists(head1, head2):
    head0 = None
    head = head0
    
    if head1 is None and head2 is not None:
        return head2
    if head2 is None and head1 is not None:
        return head1
     
    while head1 is not None or head2 is not None:
        
        if head1 is None and head2 is not None:
            if head is None:
                head = SinglyLinkedListNode(head2.data)
                head2 = head2.next
                head0=head
            else:
                head0.next = SinglyLinkedListNode(head2.data)
                head0 = head0.next
                head2 = head2.next
        if head2 is None and head1 is not None:
            if head is None:
                head = SinglyLinkedListNode(head1.data)
                head1 = head1.next
                head0=head
            else:
                head0.next = SinglyLinkedListNode(head1.data)
                head0 = head0.next
                head1 = head1.next
        
        if head1 is not None and head2 is not None:
            if head1.data<head2.data:
                if head is None:
                    head = SinglyLinkedListNode(head1.data)
                    head1 = head1.next
                    head0=head
                else:
                    head0.next = SinglyLinkedListNode(head1.data)
                    head0 = head0.next
                    head1 = head1.next
            else:
                if head is None:
                    head = SinglyLinkedListNode(head2.data)
                    head2 = head2.next
                    head0=head
                else:
                    head0.next = SinglyLinkedListNode(head2.data)
                    head0 = head0.next
                    head2 = head2.next
          
    #while head is not None:
    #    print(head.data)
    #    head=head.next       
                
    return head

