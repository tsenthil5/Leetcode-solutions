class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        postfix = []
        currMax = -1
        for index in range(len(nums)-1, -1, -1):
            if nums[index] > currMax:
                currMax = nums[index]
            postfix.insert(0, currMax)

        left, right = 0, 0
        maxRamp = -1
        #print(postfix)
        while right!=len(nums):
            #print("right", nums[right])
            #print("postfix", postfix[right])
            
            if nums[left] <= postfix[right]:
                maxRamp = max(maxRamp, right-left)
                right+=1

            else:
                left+=1
            
            

        return maxRamp


        