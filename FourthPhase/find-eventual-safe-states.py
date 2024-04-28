class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        my_graph={i:set() for i in range(len(graph))}
        indegree={i:0 for i in range(len(graph))}
        queue=deque()
        safe_nodes=[]
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                my_graph[graph[i][j]].add(i)

        for i in range(len(graph)):
            indegree[i]=len(graph[i])
            if len(graph[i])==0:
                queue.append(i)
       
        while queue:
            node=queue.popleft()
            safe_nodes.append(node)
            for neighbour in my_graph[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        safe_nodes.sort()
        return safe_nodes
                    
                

        



        
        

        