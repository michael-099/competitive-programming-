# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Set=set()
        current=head
        prev=None
        while current:
            if current.val not in Set:
                Set.add(current.val)
                prev=current
                current=current.next
            else:
                prev.next=current.next 
                current=prev.next
        return head



                




    # def remove(self,head:Optional[ListNode],index:int)-> None:
        

        