# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(left,right):
            if not right and not left:
                return True 
            if not right or not left:
                return False
            return(right.val==left.val and traverse(left.left,right.right) and traverse(left.right,right.left))
        return traverse(root.left,root.right)

        