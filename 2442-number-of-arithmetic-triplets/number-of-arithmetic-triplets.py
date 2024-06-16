class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        hashSet = set(nums)
        res = 0
        for num in nums:
            iteration = 2
            while iteration > 0:
                if num+diff in hashSet:
                    num = num+diff
                    iteration-=1

                else:
                    break

            if iteration == 0:
                res+=1

        return res
        