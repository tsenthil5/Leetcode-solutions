class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(i.split(":")[1]) for i in timePoints]
        hours = [int(i.split(":")[0]) for i in timePoints]
        timePoints = []
        for mints, hr in zip(minutes, hours):
            timePoints.append(mints+(hr*60))

        timePoints.sort()
        print(timePoints)
        minTime = float('inf')
        for idx in range(0, len(timePoints)-1):
            minTime = min(minTime, timePoints[idx+1]-timePoints[idx])


        if (timePoints[-1]-timePoints[0]) > 720:
            minTime = min(minTime, (1440-timePoints[-1] + timePoints[0]))

        return minTime


        


        '''



        '''
        
        