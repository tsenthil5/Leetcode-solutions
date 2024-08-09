class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        currSum = 0
        subDict = {0:-1}
        
        for idx, num in enumerate(nums):
            
            currSum+=num
            currRem = currSum%k
            if currRem not in subDict:
                subDict[currRem] = idx
            elif idx - subDict[currRem] > 1:
                return True

        return False

        