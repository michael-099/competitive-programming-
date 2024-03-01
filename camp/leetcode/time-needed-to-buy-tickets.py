class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        m = max(tickets)
        queue = []
        time = 0
        for i in range(m):
            for j in range(len(tickets)):
                if tickets[j] > 0:
                    queue.append(j)
                    tickets[j] -= 1
                    
        for i in range(len(queue) - 1, -1, -1):
            if k == queue[i]:
                time = i + 1
                break
        return time
