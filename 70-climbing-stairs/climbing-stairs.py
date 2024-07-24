class Solution:
    def climbStairs(self, n: int) -> int:

        def backtracking(n):
            if n in cache:
                return cache[n]
            if n == 0:
                return 1
            elif n < 0:
                return 0

            val = backtracking(n-1) + backtracking(n-2)
            cache[n] = val
            return val


        
        cache = {}
        return backtracking(n)