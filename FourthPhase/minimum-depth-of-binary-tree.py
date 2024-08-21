# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_tree = self.minDepth(root.left)
        right_tree = self.minDepth(root.right)
        print(min(left_tree,right_tree))
        return (
            min(left_tree, right_tree) + 1
            if min(left_tree, right_tree) != 0
            else max(left_tree, right_tree)+1
        )
