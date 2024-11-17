# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # do a dfs then while doing that you are going to nend a fuction who will calculate the tilt and stoer it for leter returning the sum 
        tilt=[]
        def sum_subtree(curr_root):
            the_sum=0
            def dfs(root):
                nonlocal the_sum
                if not root:
                    return 0
              
                dfs(root.left)
                the_sum+=root.val
                dfs(root.right)
            dfs(curr_root)
            # print("the sum is ", the_sum)
            return the_sum

        def calcualte_tilt(curr_root):
            # print("i am running too")
            return abs(sum_subtree(curr_root.left)-sum_subtree(curr_root.right))
        
        def dfs(root):
            if not root :
                return 

            dfs(root.left)
            tilt.append(calcualte_tilt(root))
            dfs(root.right)
        dfs(root)
        # print(tilt)
        return sum(tilt)

        