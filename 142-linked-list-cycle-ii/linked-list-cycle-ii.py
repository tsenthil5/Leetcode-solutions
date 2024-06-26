# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow, fast = head, head.next
        while slow!=fast:
            if not fast or not fast.next:
                return None

            else:
                slow = slow.next
                fast = fast.next.next

        fast = fast.next
        visited = set()
        while fast != slow:
            visited.add(fast)
            fast = fast.next
        visited.add(fast)

        start = head
        while start not in visited:
            start = start.next

        return start
        