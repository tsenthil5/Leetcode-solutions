import heapq as hq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        [ , (2, 'A', 0), (2, 'A', 0)] 


        'A' -> 'B' -> 
        '''

        countDict = {}
        for task in tasks:
            countDict[task] = countDict.get(task, 0) + 1

        maxHeap = []
        for key, values in countDict.items():
            maxHeap.append(-1*values)

        time = 0
        queue = deque([])
        hq.heapify(maxHeap)

        while maxHeap or queue:
            time+=1
            if maxHeap:
                val = hq.heappop(maxHeap)
                if val+1:

                    queue.append((val+1,time+n))
            
            if queue:
                if queue[0][1] == time:
                    hq.heappush(maxHeap, queue[0][0])
                    queue.popleft()

            

        return time


        

        



        