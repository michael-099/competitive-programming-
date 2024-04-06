class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = {}
        for card in deck:
            count[card] = count.get(card, 0) + 1
    
        freqs = count.values()
        divisor = reduce(gcd, freqs)
        
        if divisor == 1:
            return False
        for freq in freqs:
            if freq % divisor != 0:
                return False
        return True
