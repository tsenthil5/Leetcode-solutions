# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:



        def checkTree(p, q):
            if not p and not q:
                return True
            elif not p and q:
                return False

            elif p and not q:
                return False

            elif p.val != q.val:
                return False
            

            if (checkTree(p.left, q.right) and checkTree(p.right, q.left)) == False:
                return False

            return True

        return checkTree(root.left, root.right)

        