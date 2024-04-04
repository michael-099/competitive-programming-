class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for edge1,edge2 in edges:
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)
        visited=set()
        res=False
        def dfs(vertex):
            nonlocal res 
            if destination == vertex:
                return True
            
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    res=dfs(neighbor)
                    if res:
                        break 
            return res

        return dfs(source)

                    


        