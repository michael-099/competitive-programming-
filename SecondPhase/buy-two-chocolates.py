class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
       
        #    O(n)
        # for i in range(0,len(prices)):
        #     for j in range(i+1,len(prices)):
        #         print(prices[j])
        #         if prices[i]+prices[j]<=money:
        #             return money-(prices[i]+prices[j])
        # return money

        # o(nlogn)
        # prices.sort()
        # if prices[0]+prices[1]<=money:
        #     return money-(prices[0]+prices[1])
        # return money

        first_min=min(prices)
        prices.remove(first_min)
        second_min=min(prices)
        return money-(first_min+second_min) if first_min+second_min <=money else money

            

        