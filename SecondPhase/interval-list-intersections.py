class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        left = 0
        right = 0
        arr = []
        while left < len(firstList) and right < len(secondList):
            if max(firstList[left][0], secondList[right][0]) <= min(firstList[left][1], secondList[right][1]):
                arr.append(
                    [
                        max(firstList[left][0], secondList[right][0]),
                        min(firstList[left][1], secondList[right][1])
                    ]
                )
            if firstList[left][1] > secondList[right][1]:
                right += 1
            else:
                left += 1
        return arr
