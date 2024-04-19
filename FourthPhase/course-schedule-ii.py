class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph,indegree,queue,res=defaultdict(list),defaultdict(int),deque(),[]
        
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course]+=1
        
        for node in range(numCourses):
            if not indegree[node]:
                queue.append(node)
        
        while queue:
            node=queue.popleft()
            res.append(node)
            
            for neighbour in graph[node]:
                if indegree[neighbour]>0:
                    indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)

        if len(res)!=numCourses:
            return []

        return res    
            

        
        
            
        
       

        