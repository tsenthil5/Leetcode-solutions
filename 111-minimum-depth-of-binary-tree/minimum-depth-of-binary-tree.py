# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)
        if leftHeight == 0 or rightHeight == 0:
            return max(leftHeight, rightHeight)+1

        else:
            return min(leftHeight, rightHeight)+1
        