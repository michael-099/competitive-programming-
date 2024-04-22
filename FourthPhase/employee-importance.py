"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph=defaultdict(list)
        visited=set()
        for i in range(len(employees)):
            graph[employees[i].id]=[employees[i].importance,employees[i].subordinates]

        print(graph)
        def bfs(node):
            queue = deque()
            queue.append(node)
            total=graph[node][0]
            visited.add(node)

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbour in graph[node][1]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)
                            total+=graph[neighbour][0]
            return total
        
        return bfs(id)

       

    
        