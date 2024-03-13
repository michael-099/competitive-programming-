# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.find(root,root.val,root.val )
        
    def find(self,root,maximum,minimum ):
        if not root:
            return abs(maximum-minimum)
        maximum=max(root.val,maximum)
        minimum=min(root.val,minimum)    

        left=self.find(root.left,maximum,minimum)    
        right=self.find(root.right,maximum,minimum)

        return max(left,right)
