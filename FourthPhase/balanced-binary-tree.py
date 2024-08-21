# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        Flag=[True]
        def BalancedCheck(root):
            if not root:
                return 0

            left_tree=BalancedCheck(root.left)
            right_tree=BalancedCheck(root.right)
            if abs(left_tree-right_tree)>1:
                Flag[0]=False 
            return max(left_tree,right_tree)+1

        BalancedCheck(root)
        return Flag[0]

        