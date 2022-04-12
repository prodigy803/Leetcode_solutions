# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## ALTERNATIVE APPROACH FROM NEETCODE:
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        return False
        
class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # print(p)
        # print(q)
        stack = []
        p_values = []
        q_values = []
        stack.append(p)
        
        while stack != []:
            current_root = stack.pop()
            
            if current_root != None:
                p_values.append(current_root.val)
                stack.append(current_root.left)
                stack.append(current_root.right)
            else:
                p_values.append(None)    
                
        stack.append(q)
        
        while stack != []:
            current_root = stack.pop()
            
            if current_root != None:
                q_values.append(current_root.val)
                stack.append(current_root.left)
                stack.append(current_root.right)
            else:
                q_values.append(None)
                
        setter = True
        for i, j in zip(p_values, q_values):
            
            if str(i)!=str(j):
                setter = False
                break
        print('setter ', setter)
        return setter
        