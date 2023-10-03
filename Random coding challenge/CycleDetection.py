

def has_cycle(head):
    num=[]
    while head is not None: 
        if num.count(head)==0:
            num.append(head)
            head=head.next
        else:
            return 1
        
    return 0

