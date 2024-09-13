class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(currSum, currArray, index):
            if currSum == target:
                res.append(currArray.copy())
                return

            if currSum > target:
                return 

            if index == len(candidates):
                return

            currArray.append(candidates[index])
            currSum+=candidates[index]
            backtrack(currSum, currArray, index)
            currArray.pop()
            currSum-=candidates[index]
            backtrack(currSum, currArray, index+1)


        res = []
        candidates.sort()
        backtrack(0, [], 0)
        return res
        