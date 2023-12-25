class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        s=set()
        for i in range(len(backs)):
            if backs[i] == fronts[i]:
                s.add(backs[i])
        card=inf
        for i in (fronts+backs):
            if i not in s:
                card=min(card,i)
        return card if card!= inf else 0 
        


        


        