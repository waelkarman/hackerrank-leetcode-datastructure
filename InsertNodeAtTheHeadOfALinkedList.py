
def insertNodeAtHead(llist, data):
    # Write your code here
    a = SinglyLinkedListNode(data)
    a.next = llist
    return a


