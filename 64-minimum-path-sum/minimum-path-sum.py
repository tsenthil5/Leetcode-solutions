class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if (row, col) in cache:
                return cache[(row, col)]
            if row >= len(grid) or col >= len(grid[0]):
                return float('inf')
            
            if row == len(grid)-1 and col == len(grid[0])-1:
                return grid[row][col]

            
            minVal = float('inf')
            minVal = min(minVal, dfs(row+1,col),
            dfs(row, col+1))
            cache[(row, col)] = minVal + grid[row][col]
            
            return minVal + grid[row][col]


        cache = {}
        return dfs(0,0)
        