#(9.)Write a Python program to check whether a given a binary tree is a valid binary search                 tree (BST) or not.  
#Let a binary search tree (BST) is defined as follows: The left subtree of a node contains only nodes with keys less than the node's key. 
#The right subtree of a node contains only nodes with keys greater than the node's key. 
#Both the left and right subtrees must also be binary search trees.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_BST(root):
    stack = []
    prev = None
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.val <= prev.val:
            return False
        prev = root
        root = root.right
    return True

root = TreeNode(2)  
root.left = TreeNode(1)  
root.right = TreeNode(3) 
 
result = is_BST(root)
print(result)

root = TreeNode(1)  
root.left = TreeNode(2)  
root.right = TreeNode(3) 
 
result = is_BST(root)
print(result)
