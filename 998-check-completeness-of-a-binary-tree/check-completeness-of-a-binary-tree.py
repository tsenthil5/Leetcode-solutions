# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def bfs():
            queue = deque([root])
            nullFlag = False
            while queue:
                lenQ = len(queue)
                for i in range(lenQ):
                    node = queue.popleft()
                    if not node.left:
                        nullFlag = True

                    if node.left:
                        if nullFlag == True:
                            return False

                        queue.append(node.left)
                    if not node.right:
                        nullFlag = True
                        
                    if node.right:
                        if nullFlag == True:
                            return False
                        queue.append(node.right)

            return True

        return bfs()


        