# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        if not k:
            return [target.val]

        def convertToGraph(root):
            queue = deque()
            queue.append(root)
            graph = defaultdict(list)

            while queue:
                node = queue.pop()
                if node.left:
                    queue.append(node.left)
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                if node.right:
                    queue.append(node.right)
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
            return graph

        graph = convertToGraph(root)
        # print(graph[target.val])
        queue, visited = deque(),set()
        queue.append(target.val)
        visited.add(target.val)
        level=[]

        while queue:

            res=[]
            for i in range(len(queue)):
                node=queue.popleft()
                # print(graph[node])
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        res.append(neighbor)
                        queue.append(neighbor)
                        visited.add(neighbor)
                # print(res)
            level.append(res)
        # print(level)
        # print(level[k-1])
        return level[k-1] if k<=len(level) else []
        
        
                
