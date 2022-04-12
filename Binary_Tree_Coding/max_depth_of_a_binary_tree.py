class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        stack = []
        if root:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
        
            if root != None:
                depth = max(depth, current_depth)
                stack.append((current_depth+1, root.left))
                stack.append((current_depth+1, root.right))
        
        return depth