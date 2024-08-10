import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createBST(startIdx, endIdx):
            if startIdx > endIdx:
                return
            if startIdx == endIdx:
                newNode = TreeNode(nums[startIdx])
                return newNode


            mid = math.ceil((startIdx + endIdx)/2)
            parent = TreeNode(nums[mid])
            parent.left = createBST(startIdx, mid-1)
            parent.right = createBST(mid+1, endIdx)
            return parent

        return createBST(0, len(nums)-1)