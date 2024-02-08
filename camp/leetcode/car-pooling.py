class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        running_sum = 0
        max_len = max(trips, key=lambda x: x[2])[2]
        arr = [0] * (max_len + 2)
        prefix = []

        for i in range(len(trips)):
            arr[trips[i][1]] += trips[i][0]
            arr[trips[i][2] ] -= trips[i][0]

        for i in range(len(arr)):
            running_sum += arr[i]
            prefix.append(running_sum)
        print(arr)
        print(prefix)
        return capacity >= max(prefix)
