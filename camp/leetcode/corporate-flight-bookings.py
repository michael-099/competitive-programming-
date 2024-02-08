class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr=[0]*(n+2)
        for i in range(len(bookings)):
            arr[bookings[i][0]]+=bookings[i][2]
            arr[bookings[i][1]+1]-=bookings[i][2]
        running_sum=0 
        for i in range(len(arr)):
            running_sum+=arr[i]
            arr[i]=running_sum
        return arr[1:-1]

            
        