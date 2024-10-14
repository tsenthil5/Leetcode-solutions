import heapq as hq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-1*x for x in nums]
        hq.heapify(nums)
        score = 0
        while k!=0:
            val = hq.heappop(nums)
            score+=val
            hq.heappush(nums, -1*math.ceil(-1*(val/3)))
            k-=1
        return -1*score
            


        