class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        def backtracking(ptr):
            if ptr == len(s):
                return 0
            if ptr == len(s)-1:
                return hashmap[s[ptr]]

            if hashmap[s[ptr]] < hashmap[s[ptr+1]]:
                return hashmap[s[ptr+1]] - hashmap[s[ptr]] + backtracking(ptr+2)


            return hashmap[s[ptr]] + backtracking(ptr+1)


        return backtracking(0)

            

            


        