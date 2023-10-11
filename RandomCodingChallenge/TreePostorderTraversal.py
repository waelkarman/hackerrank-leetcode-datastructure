

def postOrder(root):
    #Write your code here
    # left right root
    
    if root.left is not None:
        postOrder(root.left)
        
    if root.right is not None:
        postOrder(root.right)
        
    print(root.info,end=' ')



