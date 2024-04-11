class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue,visited=deque(),set(deadends)
        queue.append(["0000",0])
        if "0000" in visited:
            return -1
        def generate(node):
            res=[]
            for i in range(4):
                res.append(node[:i]+str(((int(node[i])+1)+10)%10)+node[i+1:])
            for i in range(4):
                res.append(node[:i]+str(((int(node[i])-1)+10)%10)+node[i+1:])
            return res 
                
        while queue:

            for _ in range(len(queue)):
                node,length=queue.popleft()
                if node == target:
                    return length
                possibilities = generate(node)
                
                for possibility in  possibilities :
                    if possibility not in visited:
                        queue.append([possibility,length+1])
                        visited.add(possibility)
        return -1

                

                
                



      
     

        