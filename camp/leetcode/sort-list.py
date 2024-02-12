# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None : return None 
        arr=[]
        current=head
        while current:
            arr.append(current.val)
            current=current.next
            
        arr.sort()
        curr=head
        for i in range(len(arr)):
            curr.val=arr[i]
            curr=curr.next
        return head
            
        

        