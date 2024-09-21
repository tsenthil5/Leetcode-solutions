# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left = list1
        count = 0
        while count != a-1:
            left = left.next
            count+=1

        right = left
        while count != b:
            right = right.next
            count+=1

        left.next = list2
        end = list1
        while end.next!= None:
            end = end.next

        if right.next == None:
            end.next = None

        else:
            end.next = right.next

        return list1

            
        