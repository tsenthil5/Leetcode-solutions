class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        def shiftChar(char, shift):
            asc = ord(char)+shift
            
            while(asc > ord('z')):
                diff = asc - 122
                asc = 96 + diff


            
            return chr(asc)
        
        
        postfix = []
        currSum = 0
        shifts.reverse()
        for num in shifts:
            currSum+=num
            if currSum > 26:
                currSum = currSum % 26
            postfix.insert(0, currSum)
        
        res = ""
        #print(postfix)
        for idx, shift in enumerate(postfix):
            res+=shiftChar(s[idx], shift)

        return res

        