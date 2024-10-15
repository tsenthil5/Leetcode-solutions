class Solution:
    def minimumSteps(self, s: str) -> int:
        '''

        1010011
        '''

        endPtr = len(s)-1
        steps = 0
        currZero = 0
        while endPtr>=0:
            if s[endPtr] == "0":
                currZero+=1

            else:
                steps+=currZero

            endPtr-=1
        return steps

        