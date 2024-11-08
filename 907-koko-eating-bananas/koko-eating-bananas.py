class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxVal = max(piles)
        left, right = 1, maxVal
        minK = maxVal

        def calcK(k):
            totalH = 0
            for i in piles:
                totalH+=math.ceil(i/k)
            return totalH


        while(left<=right):
            mid = (left+right)//2
            if calcK(mid) >h:
                left = mid+1


            else:
                minK = mid
                right = mid-1

        return minK
        