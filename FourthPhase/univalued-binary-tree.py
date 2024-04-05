# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val=root.val
        queue=deque()
        queue.append(root)


        while queue:
            node=queue.popleft()
            print(node)

            if val != node.val:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True



        