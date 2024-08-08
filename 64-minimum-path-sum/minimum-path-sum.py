class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        123
        456
        '''
        def dp(startIdx, endIdx):
            if startIdx < 0 or endIdx < 0 or startIdx >= len(grid) or endIdx >= len(grid[0]):
                return float('inf')
            if (startIdx, endIdx) in cache:
                return cache[(startIdx, endIdx)]

            if startIdx == len(grid)-1 and endIdx == len(grid[0])-1:
                return grid[startIdx][endIdx]

            cache[(startIdx, endIdx)] = min(dp(startIdx+1, endIdx), dp(startIdx, endIdx+1)) + grid[startIdx][endIdx]
            return cache[(startIdx, endIdx)]
            

        cache = {}
        return dp(0, 0)
        