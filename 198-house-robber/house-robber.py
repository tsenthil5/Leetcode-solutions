class Solution:
    def rob(self, nums: List[int]) -> int:



        def backtracking(pointer):
            if pointer > len(nums)-1:
                return 0
            if pointer == len(nums)-1:
                return nums[pointer]
            if pointer in cache:
                return cache[pointer]

            maxVal = 0
            for i in range(pointer+2, len(nums), 1):
                val = backtracking(i)
                maxVal = max(val, maxVal)
            cache[pointer] = maxVal + nums[pointer]
            return cache[pointer]
            
            
        maxVal = 0
        cache = {}
        for i in range(0,len(nums), 1):
            val = backtracking(i)
            maxVal = max(val, maxVal)
        return maxVal
            
        