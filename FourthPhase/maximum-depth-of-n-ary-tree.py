"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def bfs(root):
            if not root:
                return 0
            queue=deque()
            queue.append(root)
            depth=0
            while queue: 
                for i in range(len(queue)):
                    curr=queue.popleft()
                    for child in curr.children:
                        queue.append(child)
                depth+=1
            return depth 
        
        def dfs(root):
            depth=0
            if not root:
                return 0
            for child in root.children:
                depth=max(depth,dfs(child))
            return depth+1
   
        return dfs(root)  
                



        