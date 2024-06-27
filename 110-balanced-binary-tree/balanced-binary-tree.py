# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def checkHeight(root):
            if not root:
                return 0
            leftHeight = checkHeight(root.left)
            rightHeight = checkHeight(root.right)
            #print("leftHeight", leftHeight)
            #print("rightHeight", rightHeight)
            if type(leftHeight) == bool or type(rightHeight) == bool:
                return False
            elif abs(leftHeight-rightHeight) > 1:
                return False

            else:
                return max(leftHeight, rightHeight)+1

        
        if type(checkHeight(root)) != bool:
            return True
        else:
            return False 
        

        