def findMergeNode(head1, head2):

    h2_back = head2
    i=0
    j=0
    
    while head1 is not None:
        head2 = h2_back
        while head2 is not None:
            if head1 == head2 and head1 is not None:
                #print("found:", head1.data)
                return head1.data
                head2 = head2.next
            else:
                head2 = head2.next
            j+=1
            
        head1 = head1.next
        i+=1


