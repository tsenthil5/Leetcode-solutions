class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        res = 0
        for idx, num in enumerate(nums):
            curr = idx+1
            count = 1
            while curr!=len(nums):
                if nums[curr] - num > diff:
                    break
                elif nums[curr] - num == diff:
                    count+=1
                    num = nums[curr]
                    if count == 3:
                        res+=1
                curr+=1

        return res

        '''
res = 0
curr = 1
num = 0
    1<3
    4>3
curr = 2
num = 4
    count = 2
        '''









        