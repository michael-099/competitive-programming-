# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def average(arr):
            return sum(arr)/len(arr)

        queue=deque()
        queue.append(root)
        res=[]

        while queue:
            tem =[]
            for i in range(len(queue)):
                tem.append(queue[i].val)
            if tem:
                res.append(average(tem))

            for i in range(len(queue)):
                node =queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

        
        


        