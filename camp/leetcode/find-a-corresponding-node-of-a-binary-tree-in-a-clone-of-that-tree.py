# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def Target(root1,root2):
            # print(target)
            if not root1 and not root2:
                return
            
            print(root2.val )
            if root2.val==target.val:
                return root2

            val1=Target(root1.left,root2.left)
            val2=Target(root2.right,root2.right)
            return val1 if val1 else val2
        return Target(original,cloned)
        
        
        