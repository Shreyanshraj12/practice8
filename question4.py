class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(s):
    if not s:
        return None
    
  
    index = s.find('(')
    if index == -1:
       
        return TreeNode(int(s))
   
    node = TreeNode(int(s[:index]))
    
    
    count = 0
    i = index
    while i < len(s):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
            if count == 0:
                break
        i += 1
    
   
    left_subtree = s[index+1:i]
    right_subtree = s[i+2:-1]
    
   
    node.left = buildTree(left_subtree)
    node.right = buildTree(right_subtree)
    
    return node

def inorderTraversal(root):
    if root is None:
        return []
    
    result = []
    result += inorderTraversal(root.left)
    result.append(root.val)
    result += inorderTraversal(root.right)
    
    return result


s = "4(2(3)(1))(6(5))"
root = buildTree(s)
result = inorderTraversal(root)
print(result)  
