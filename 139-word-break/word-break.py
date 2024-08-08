class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Understand
        any edge cases?
        empty strings? 
        min length of 1


        Match
        DP
        Memoization
        String iteration

        Plan
        iterate through string and check if word is in string
        iterate through list 
        check if word is in cache
        check if word is present in the string
        store it in cache
        '''

        def dp(startIdx, endIdx):
            #print(s[startIdx: endIdx+1])
            if s[startIdx:endIdx+1] in cache:
                return cache[s[startIdx:endIdx+1]]
            if s[startIdx:endIdx+1] == "":
                return True

            for i in range(startIdx, endIdx):
                if dp(startIdx, i) == True and dp(i+1, endIdx) == True:
                    cache[s[startIdx:endIdx+1]] = True
                    
                    return True

                #if s[startIdx:i] in cache:
                    
                 #   if dp(i,endIdx) == True:
                  #      cache.add(s[i:endIdx+1])
                   #     return True

            cache[s[startIdx:endIdx+1]] = False
            return False
                    

        cache = {}
        for word in wordDict:
            cache[word] = True

        return dp(0, len(s))

        
