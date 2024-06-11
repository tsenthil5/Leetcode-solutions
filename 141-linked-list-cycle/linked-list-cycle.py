# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        tempSlow, tempFast = head, head.next
        while tempSlow and tempFast:
            if tempSlow == tempFast:
                return True

            else:
                tempSlow = tempSlow.next
                if tempFast.next != None:
                    tempFast = tempFast.next.next
                else:
                    break

        return False
        