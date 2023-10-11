
def inOrder(root):
    #Write your code here

    if root.left is not None:
        inOrder(root.left)

    print(root.info,end=' ')
    
    if root.right is not None:
        inOrder(root.right)
        
        



















