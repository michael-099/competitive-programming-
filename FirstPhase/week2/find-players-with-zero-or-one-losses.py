class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # matches       
        winners={}
        losers={}
        for i in range (len(matches)) :
            winners[matches[i][0]]=winners.get(matches[i][0],0)+1
            losers[matches[i][1]]=losers.get(matches[i][1],0)+1
        print( winners,losers)
        not_lost_any_matches=[x for x in winners if x in winners and  x not in losers ]
        not_lost_any_matches.sort()
        have_lost_exactly_one_match=[x for x,v in losers.items() if v == 1]
        have_lost_exactly_one_match.sort()
        return[ not_lost_any_matches, have_lost_exactly_one_match]