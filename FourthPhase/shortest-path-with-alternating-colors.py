class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red=defaultdict(list)
        blue=defaultdict(list)
        answer,queue,visited=[-1 for i in range(n)],deque(),set()

        for start,dist in redEdges:
            red[start].append(dist)
        for start,dist in blueEdges:
            blue[start].append(dist)
        
        queue.append([0,0,None])
        visited.add ((0,None))

        while queue:
            node,length,prev_color=queue.popleft()
            if answer[node]==-1:
                answer[node]=length
            
            
            if prev_color != "RED":
                for neighbor in red[node]:
                    if(neighbor,"RED") not in visited:
                        queue.append([neighbor,length+1 ,"RED"])
                        visited.add((neighbor,"RED"))
            if prev_color != "BLUE":
                for neighbor in blue[node]:
                    if(neighbor,"BLUE") not in visited:
                        queue.append([neighbor,length+1,"BLUE"])
                        visited.add((neighbor,"BLUE"))
        return answer
                

                    
                

            
        


        




        return answer


        