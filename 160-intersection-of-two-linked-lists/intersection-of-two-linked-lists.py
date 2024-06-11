# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        lenA = 0
        while(tempA!=None):
            lenA+=1
            tempA = tempA.next
        tempB= headB
        lenB = 0
        while(tempB!=None):
            lenB+=1
            tempB = tempB.next

        if lenB > lenA:
            while lenB != lenA:
                headB = headB.next
                lenB-=1

        elif lenB < lenA:
            while lenB!=lenA:
                headA = headA.next
                lenA-=1
        while headA or headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
        