# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq as hq
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        max_heap = []
        hq.heapify(max_heap)
        def bfs():

            queue = deque([root])
            while queue:
                levelSum = 0
                for _ in range(len(queue)):
                    node = queue.popleft()
                    levelSum+=node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                hq.heappush(max_heap, -1*levelSum)
        
        bfs()
        if k > len(max_heap):
            return -1

        else:
            while k!=1:
                hq.heappop(max_heap)
                k-=1

            return -1*hq.heappop(max_heap)
        