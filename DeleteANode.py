
def deleteNode(llist, position):
    # Write your code here
    #print("positionnnn ",position)
    if llist is None:
        return None
    if position == 0:
        llist = llist.next
        return llist
        
    #if position == 1:
    #    llist.next = llist.next.next
    #    return llist
        
    first = llist
        
        
    while position > 1:
        llist = llist.next
        position -= 1
    
    llist.next = llist.next.next
        
    return first


