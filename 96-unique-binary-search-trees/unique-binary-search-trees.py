class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n<=1:
            return 1


        total = 0
        for i in range(1,n+1):
            leftChild = self.numTrees(i-1)
            rightChild = self.numTrees(n-i)
            total+=leftChild*rightChild

        return total
        