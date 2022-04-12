# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# SOLUTION FROM NEETCODE
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True

        if root == None:
            return False

        if self.isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            
    def isSame(self, root, subRoot):
        if root == None and subRoot == None:
            return True

        if root and subRoot and root.val == subRoot.val and (self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)):
            return True
            
        return False


# MY SOLUTION
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # stack_root = []
        stack_sub_root = []
        comparison_stack_root = []
        comparison_stack_subroot = []
        stack_root = [root]
        
        while stack_root != []:
            current_root = stack_root.pop()
            if current_root != None:
                current_root_val = current_root.val
                # print(current_root_val, subRoot.val)
                if (current_root_val == subRoot.val):
                    returned_val = self.isSameTree(current_root, subRoot)
                    if returned_val == True:
                        return returned_val
                
                stack_root.append(current_root.left)
                stack_root.append(current_root.right)
        return False
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # print(p)
        # print(q)
        stack = []
        p_values = []
        q_values = []
        stack.append(p)
        
        while stack != []:
            current_root = stack.pop(0)
            
            if current_root != None:
                p_values.append(current_root.val)
                stack.append(current_root.left)
                stack.append(current_root.right)
            else:
                p_values.append(None)
                
        stack.append(q)
        
        while stack != []:
            current_root = stack.pop(0)
            
            if current_root != None:
                q_values.append(current_root.val)
                stack.append(current_root.left)
                stack.append(current_root.right)
            else:
                q_values.append(None)
                
        setter = True
        for i, j in zip(p_values, q_values):
            
            if i != j:
                setter = False
                break
        # print('setter ', setter)
        return setter