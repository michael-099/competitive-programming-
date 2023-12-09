class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if (start<=destination):
           sum1=sum(distance[start:destination])
           sum2=sum(distance)-sum1
           return  min(sum1,sum2)
        else:
            sum1=sum(distance[destination:start])
            sum2=sum(distance)-sum1
            print(sum1)
            return min (sum1,sum2)
            # return  min(,sum(distance[0:start+1])-sum(distance[destination:start]))
        # return 0
        # 0 0+1%n 1    1
        # 1 1+1%n 2    2
        # 2 2+1%n 3    3
        # 3 3+1%n 0    4      
        
        