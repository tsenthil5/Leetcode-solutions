class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sumLength = float(sum(matchsticks)//4)
        if sum(matchsticks)/4 != sumLength:
            return False

        matchsticks.sort(reverse = True)
        side = [0]*4

        def backtracking(idx):
            if idx == len(matchsticks):
                return True

            for j in range(4):
                if side[j] + matchsticks[idx] <= sumLength:
                    side[j]+=matchsticks[idx]
                    if backtracking(idx+1) == True:
                        return True
                    side[j]-=matchsticks[idx]

            return False
        
        return backtracking(0)


        