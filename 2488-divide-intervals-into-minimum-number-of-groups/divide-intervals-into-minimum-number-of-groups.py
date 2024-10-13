class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        startVal = [x[0] for x in intervals]
        endVal = [x[1] for x in intervals]
        startVal.sort()
        endVal.sort()
        left, right = 0, 0
        groups = 0
        res = 0
        while left<len(intervals):
            if startVal[left] <= endVal[right]:
                left+=1
            else:
                
                right+=1

            res = max(res, left-right)

        return res
            
        