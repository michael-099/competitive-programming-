# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merge(left_tree,right_tree):
            if not left_tree :
                return right_tree
            if  not right_tree:
                return left_tree

            left_tree.val+=right_tree.val
            left_tree.left=merge(left_tree.left,right_tree.left)
            left_tree.right=merge(left_tree.right,right_tree.right)
            return left_tree
        
        return merge(root1,root2)
