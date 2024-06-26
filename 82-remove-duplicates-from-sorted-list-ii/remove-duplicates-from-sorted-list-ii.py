# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
         #create dummy
         #assifgn dummy -> prev
         #loop until curr!=curr.next
         #assign prev.next = curr.next
         
        dummy = ListNode()
        prev = dummy
        prev.next = head
        curr = head

        while curr and curr.next:
            flag = 0
            while curr.val == curr.next.val:
                curr = curr.next
                flag = 1
                if not curr.next:
                    prev.next = None
                    break
            if flag == 1:
                if curr:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next


        return dummy.next
            

        