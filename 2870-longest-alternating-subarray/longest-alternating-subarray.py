class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        '''

        [4,7,9] => -1
        [1,2,3,4,5,6] => 2


        1) leftPtr, rightPtr = 0, 1
        2) if flag = 1 and rightptr- leftPtr = 1 
        3) leftPtr+=1 rightPtr+=1
        3) flag = -1
        '''



        leftPtr, rightPtr = 0, 1
        flag = 1
        maxSub = -1
        while rightPtr != len(nums):
            
            if nums[rightPtr] - nums[rightPtr-1] == flag:
                maxSub = max(maxSub, rightPtr-leftPtr+1)
                if flag == -1:
                    flag = 1
                else:
                    flag = -1
                rightPtr+=1

            else:
                if nums[rightPtr] - nums[rightPtr-1] != 1:
                    leftPtr = rightPtr
                    rightPtr+=1
                    
                else:
                    leftPtr = rightPtr-1
                flag = 1
        return maxSub




        