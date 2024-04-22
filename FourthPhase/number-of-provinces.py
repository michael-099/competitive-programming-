class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph=defaultdict(list)
        visited=set()
        provinces =0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    graph[i].append(j)
        def bfs(node):
            queue=deque()
            queue.append(node)
            visited.add(node)

            while queue:
                for _ in range(len(queue)):
                
                    node=queue.popleft()
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)
        for node in range(len(isConnected)): 
            if node not in visited:

                bfs (node)
                provinces+=1
                
            
        
   
        return provinces 