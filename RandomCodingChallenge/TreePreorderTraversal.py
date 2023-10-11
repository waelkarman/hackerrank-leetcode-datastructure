
def preOrder(root):
    #Write your code here
    # root left right
    
    if root is not None:
        print(f"{root.info}",end=' ')
        
    if root.left is not None:
        preOrder(root.left)
    
    if root.right is not None:
        preOrder(root.right)


