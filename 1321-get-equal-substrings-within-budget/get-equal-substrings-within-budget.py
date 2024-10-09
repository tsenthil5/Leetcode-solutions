class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ascii_diff = []
        for index in range(len(s)):
            ascii_diff.append(abs(ord(s[index])-ord(t[index])))

        left, right = 0, 0
        currSum = 0
        maxChange = 0
        
        while right!=len(t):
            
            if currSum + ascii_diff[right] > maxCost:
                currSum-=ascii_diff[left]
                left+=1

            else:
                currSum+=ascii_diff[right]
                maxChange = max(maxChange, right-left+1)

                right+=1

                
            

            

        return maxChange


        