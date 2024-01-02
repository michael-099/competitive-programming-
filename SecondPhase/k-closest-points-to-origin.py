class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            points.sort()
            distances={}
           
           
            def distance(self,x :int ,y:int):
                d= (x**2 ) + (y ** 2)
                return d  


            for i in range(len(points)):
                d=distance(self,points[i][0],points[i][1])
                if d not in distances:
                    distances[d]=[points[i]]
                else :
                    distances[d].append(points[i])

            key=list(distances.keys())
            key.sort()
            output=[]
            print(distances)
            for i in range(min(len(distances),k)):
                output=output+distances[key[i]]
                if len(output)==k:
                    break 
            return output