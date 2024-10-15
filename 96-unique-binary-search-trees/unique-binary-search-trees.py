class Solution:
    def numTrees(self, n: int) -> int:
        def dp(node):

            if node < 1:
                return 1

            if node in cache:
                return cache[node]

            total = 0
            for i in range(1,node+1,1):
                left = dp(i-1)
                right = dp(node-i)
                total += left*right

            cache[node] = total
            return total

        cache = {}
        return dp(n)
        
        