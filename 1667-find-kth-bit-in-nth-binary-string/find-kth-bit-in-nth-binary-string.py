class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        startString = "0"

        while len(startString) <= k:
            invertString = ""
            for i in startString:
                if i == "0":
                    invertString+="1"

                else:
                    invertString+="0"
            startString = startString + "1" + invertString[::-1]

        return startString[k-1]



        

        