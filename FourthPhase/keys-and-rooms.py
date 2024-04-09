class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dic={i:rooms[i] for i in range(len(rooms))}
        visited=[False for i in range(len(rooms))]
        visited[0]=True
        queue=deque()
        for i in range(len(rooms[0])):
            queue.append(rooms[0][i])
            visited[rooms[0][i]]=True 
        
        while queue:
            node=queue.popleft()
            for next_node in dic[node]:
                if visited[next_node]==False:
                    queue.append(next_node)
                    visited[next_node]=True
      
        for isvisited in visited:
            if not isvisited:
                return False 
        return True 
            





