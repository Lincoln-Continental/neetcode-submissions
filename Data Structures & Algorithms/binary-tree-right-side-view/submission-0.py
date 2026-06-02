# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [[root, 0]]

        while stack:
            node, depth = stack.pop()

            if node:
                if len(result) == depth:
                    result.append(node.val)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
                
        return result