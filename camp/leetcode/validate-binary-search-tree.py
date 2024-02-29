# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(root,max_val,min_val):
            
            if not root:
                return True
            print(root.val, min_val, max_val)
            
            if not (min_val <= root.val<=max_val):
                return False 
            left_ans=check(root.left,root.val-1,min_val)
            right_ans=check(root.right,max_val,root.val+1)
            return left_ans and right_ans
        return check(root,float('inf'),-float('inf'))

            

                
            