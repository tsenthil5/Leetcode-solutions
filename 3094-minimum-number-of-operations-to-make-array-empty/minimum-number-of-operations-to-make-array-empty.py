class Solution:
    def minOperations(self, nums: List[int]) -> int:
        countDict = {}
        for num in nums:
            countDict[num] = countDict.get(num, 0)+1
        minOpr = 0
        for key, value in countDict.items():
            if value == 1:
                return -1

            else:
                temp = 0
                if value%3 == 0:
                    temp+=value//3
                else:
                    if (value%3)%2 == 0:
                        temp+=value//3
                        value = value%3
                        temp+=value//2

                    else:
                        value = value-4
                        temp+=value//3
                        temp+=2
                minOpr+=temp

        return minOpr
