class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        totalSum = k * threshold
        currSum = 0
        left, right = 0, 0
        subArr = 0
        while(right-left < k):
                currSum+=arr[right]
                right+=1
        
        while(right!=len(arr)):
            
            if currSum >= totalSum:
                subArr+=1

            currSum-=arr[left]
            left+=1
            currSum+=arr[right]
            right+=1
            
        if currSum >= totalSum:
            return subArr+1
        else:

            return subArr

            
            


        