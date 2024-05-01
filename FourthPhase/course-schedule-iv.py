class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        graph = {i: set() for i in range(numCourses)}
        pres = {i: set() for i in range(numCourses)}
        indegree = {i: int() for i in range(numCourses)}
        queue = deque()
        for pre, course in prerequisites:
            graph[pre].add(course)
            indegree[course]+=1
        
        for key,value in indegree.items():
            if value==0:
                queue.append(key)
       
        while queue:
            node = queue.popleft()
            
            for neighbour in graph[node]:
                indegree[neighbour]-=1
                pres[neighbour].add(node)
                pres[neighbour].update(pres[node])

                if indegree[neighbour]==0:
                    queue.append(neighbour)
            prev=node
 
        res=[True if u in pres[v] else False for u,v in queries ]
        return res 
    


