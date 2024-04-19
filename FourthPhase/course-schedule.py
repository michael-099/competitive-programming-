class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph,indegree=defaultdict(list),defaultdict(int)
        queue,res=deque(),[]
        
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course]+=1

        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)

        while queue:
            node=queue.popleft()
            res.append(node)
            for neighbour in graph[node]:
                if indegree[neighbour] > 0 :
                    indegree[neighbour]-=1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return len(res)==numCourses

            
    



        