# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length, current, parts = 0, head, []
        while current != None:
            current = current.next
            length += 1
        size, remaining = length // k, length % k
        current = head
        for i in range(k):
            parts.append(current)
            for j in range(size - 1 + (1 if remaining else 0)):
                if not current:
                    break
                current = current.next
            if current:
                current.next, current = None, current.next
            remaining -= 1 if remaining else 0

        return parts
