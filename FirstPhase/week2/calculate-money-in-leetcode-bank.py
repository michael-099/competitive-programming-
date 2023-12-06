class Solution:
    def totalMoney(self, n: int) -> int:
        savings=0
        weeks=(n//7)+1 if n%7!=0 else int(n/7)
        print(weeks)
        counter=0
        for week in range(weeks):
            for week in range(week,7+week):
                if counter<n:
                #  print(week)
                 savings=savings+(week+1)
                 counter=counter+1
                #  print(counter)
        return savings