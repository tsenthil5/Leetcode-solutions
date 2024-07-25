# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
         
        leftVal = self.pruneTree(root.left)
        rightVal = self.pruneTree(root.right)
        if leftVal == None:
            root.left = None
        if rightVal == None:
            root.right= None

            
        if rightVal == None and leftVal == None and root.val == 0:
            return None
        else:
            return root
        