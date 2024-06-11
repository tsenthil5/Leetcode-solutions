# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        while(headA!=None):
            visited.add(headA)
            headA = headA.next

        while(headB!=None):
            if headB not in visited:
                headB = headB.next
            else:
                return headB


        return None
        