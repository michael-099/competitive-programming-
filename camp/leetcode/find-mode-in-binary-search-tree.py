# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        frequency={}
        def traverse(current):
            if not current:
                return
            traverse(current.left)
            frequency[current.val]=frequency.get(current.val,0)+1
            traverse (current.right)
            return current.val
        traverse(root)
        max_val=max(frequency.values()) if frequency else 0 
        mode=[]
        for val in frequency:
            if frequency [val]==max_val:
                mode.append(val)
        return mode




        

        