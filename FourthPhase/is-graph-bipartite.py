class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color = [-1] * n
        result = True
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                result = result and self.dfs(node, graph, color)
        return result

    def dfs(self, node, graph, color):
        for neighbour in graph[node]:
            if color[neighbour] == -1:
                color[neighbour] = 1 - color[node] 
                if not self.dfs(neighbour, graph, color):
                    return False
            elif color[neighbour] == color[node]:
                return False  
        return True
