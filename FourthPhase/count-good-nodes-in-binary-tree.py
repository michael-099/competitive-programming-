# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        count = 0

        while stack:
            top = stack.pop()

            if top[0].val >= top[1]:
                count += 1
            new_max = max(top[1], top[0].val)

            if top[0].left:
                stack.append((top[0].left, new_max))
            if top[0].right:
                stack.append((top[0].right, new_max))
            
        return count
