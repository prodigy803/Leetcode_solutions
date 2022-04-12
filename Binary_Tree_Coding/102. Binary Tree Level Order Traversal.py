# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root != None:
            stack = []
            # print(root)
            stack.append((1, root))
            depth = 0
            all_roots = [(1, root.val)]
            dict1 = {}
            while len(stack)!= 0:
                current_root = stack.pop(0)
                current_depth = current_root[0]

                if current_root[1] != None:
                    depth = max(current_depth, depth)
                    stack.append((current_depth+1, current_root[1].left))
                    stack.append((current_depth+1, current_root[1].right))

                    if current_root[1].left != None:
                        all_roots.append((current_depth+1, current_root[1].left.val))

                    if current_root[1].right != None:
                        all_roots.append((current_depth+1, current_root[1].right.val))

            # print(all_roots)
            dict1 = {}

            for root_vals in all_roots:
                try:
                    dict1[root_vals[0]].append(root_vals[1])
                except:
                    dict1[root_vals[0]] = [root_vals[1]]
            main_output = []

            for value in dict1.values():
                main_output.append(value)

            return main_output