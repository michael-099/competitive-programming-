# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete=set(to_delete)
        res=[]
        def helper(root,is_root): #we pass the root and a boolean to the functon 
            if not root:
                return 
            root_deleted=root.val in to_delete #returns a boolean if the node is in deleted
            if is_root and not root_deleted:
                res.append(root)
            root.left=helper(root.left , root_deleted)
            root.right=helper(root.right ,root_deleted)
            return None if root_deleted else root 
        helper(root,True)
        return res

            
           
            

