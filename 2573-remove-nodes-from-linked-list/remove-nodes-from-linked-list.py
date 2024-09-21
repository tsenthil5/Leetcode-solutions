# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def linkedListRev(head):
            pre, cur = head, head.next
            while cur:
                temp = cur.next
                cur.next = pre
                if pre == head:
                    pre.next = None
                pre = cur
                cur = temp
            return pre


        currMax = -1
        newHead = linkedListRev(head)
        startPtr = newHead
        prevHead = newHead
        while newHead:
            if newHead.val >= currMax:
                currMax = newHead.val
                prevHead = newHead
            else:
                prevHead.next = newHead.next 
            newHead = newHead.next

        return (linkedListRev(startPtr))


        