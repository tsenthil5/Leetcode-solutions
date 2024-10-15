# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None


        root = TreeNode(preorder[0])
        preIndex = 1
        if preIndex < len(preorder):
            mid = postorder.index(preorder[preIndex])

        else:
            return root

        root.left = self.constructFromPrePost(preorder[1:mid+2], postorder[:mid+1])
        root.right = self.constructFromPrePost(preorder[mid+2:], postorder[mid+1:len(postorder)-1])
        return root

        