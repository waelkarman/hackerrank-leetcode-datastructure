
def printLinkedList(head):
    if head is None:
        return
    if head is not None:
        print(head.data)
    printLinkedList(head.next)

