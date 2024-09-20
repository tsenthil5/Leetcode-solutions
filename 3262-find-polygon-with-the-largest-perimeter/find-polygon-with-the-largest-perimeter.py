class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
        [1,1,2,3,5,12,50]
         L   R
        '''
        if len(nums) == 2:
            return -1

        nums.sort()
        currSum = 0
        totalPerimeter = -1
        for idx in range(len(nums)-1):
            if idx >=2 and nums[idx] < currSum:
                currSum+=nums[idx]
                totalPerimeter = max(totalPerimeter, currSum)
            
            else:
                currSum+=nums[idx]

        #print(idx)
        idx+=1
        if nums[idx] < currSum:
            currSum+=nums[idx]
            totalPerimeter = max(totalPerimeter, currSum)

        return totalPerimeter


        