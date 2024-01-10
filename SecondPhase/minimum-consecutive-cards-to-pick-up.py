class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left=0 
        card_count=float('inf')
        count={}
        for right,card in enumerate(cards):
            if card not in count:
                count[card]=1 
            else:
                while cards[left]!=card and right >= left:
                    count[cards[left]]-=1
                    if count[cards[left]]==0:
                        count.pop(cards[left])
                    left=left+1 
                left+=1
                card_count=min(card_count,right-left+1)
        return card_count+1 if card_count!=float("inf") else -1
            
               
