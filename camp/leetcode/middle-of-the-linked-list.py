# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=1
        current=head
        while current.next:
             current=current.next
             length += 1
        print(length)
        mid=(length//2) if length %2 !=0 else length/2
        print(mid)
        temp=head
        for i in range(int(mid)):
            temp=temp.next
        return temp

        