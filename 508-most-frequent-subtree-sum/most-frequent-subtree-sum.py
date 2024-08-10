# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        visitedDict = defaultdict(int)
        freqsumRes = []
        freqsum = 0

        def dfs(node):
            nonlocal freqsum
            nonlocal freqsumRes
            if not node:
                return 0

            left = dfs(node.left) 
            right = dfs(node.right)
            subsum = left + right + node.val
            visitedDict[subsum]+=1
            print(visitedDict[subsum])
            print(visitedDict[freqsum])
            if visitedDict[subsum] > freqsum:
                freqsumRes = [subsum]
                freqsum = visitedDict[subsum]
                
                
            elif visitedDict[subsum] == freqsum:
                freqsumRes.append(subsum)
                
            
            
            return subsum
        
        dfs(root)
        return freqsumRes


        