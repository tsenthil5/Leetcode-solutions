# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        currCarry = 0
        newStart = ListNode()
        currStart = newStart
        while(head1 and head2):
            currTotal = head1.val + head2.val + currCarry
            newNode = ListNode(currTotal%10)
            currStart.next = newNode
            currCarry = currTotal//10
            head1 = head1.next
            head2 = head2.next
            currStart = currStart.next

        if head1:
            while(head1!=None):
                currTotal = head1.val + currCarry
                newNode = ListNode(currTotal%10)
                currStart.next = newNode
                currCarry = currTotal//10
                head1 = head1.next
                currStart = currStart.next


        elif head2:
            while(head2!=None):
                currTotal = head2.val + currCarry
                newNode = ListNode(currTotal%10)
                currStart.next = newNode
                currCarry = currTotal//10
                head2 = head2.next
                currStart = currStart.next
        if currCarry!=0:
            newNode = ListNode(currCarry)
            currStart.next = newNode
        return newStart.next

        