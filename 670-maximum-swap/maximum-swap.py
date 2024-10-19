class Solution:
    def maximumSwap(self, num: int) -> int:
        numArray = []
        while num>0:
            numArray.insert(0, num%10)
            num = num//10


        suffixArray = []
        currMax = -1
        for nums in numArray[::-1]:
            currMax = max(currMax, nums)
            suffixArray.insert(0, currMax)


        left = 0
        right = len(numArray)-1
        while left != len(numArray)-1:
            if numArray[left] < suffixArray[left+1]:
                while numArray[right]!=suffixArray[left+1]:
                    right-=1
                break

            else:
                left+=1

        numArray[left], numArray[right] = numArray[right], numArray[left]

        res = 0
        currPow = 0
        for nums in numArray[::-1]:
            res+=nums*(10**currPow)
            currPow+=1

        return res




        