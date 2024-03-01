# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        look_up = set()
        intersection = None
        currentA, currentB = headA, headB

        while currentA != None:
            look_up.add(currentA)
            currentA = currentA.next

        while currentB:
            if currentB in look_up:
                intersection = currentB
                break
            currentB = currentB.next

        return intersection
