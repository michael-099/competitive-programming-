# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(current, val):
            if not current:
                return
            if current.val == val:
                return  current     
            elif val < current.val:
                return search(current.left, val)
            elif val > current.val:
                return search(current.right, val)

        return search(root, val)
