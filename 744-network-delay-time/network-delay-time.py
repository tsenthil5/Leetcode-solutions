from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        visited = set()
        minTime = {}
        pq = []
        for node in range(1,n+1):
            if node == k:
                minTime[node] = 0
            else:
                minTime[node] = float('inf')

        
        heapq.heappush(pq, [minTime[k],k])
        
        for source, dst, weight in times:
            adjList[source].append((weight, dst))

        while pq:
            #print(pq)
            minval, node = heapq.heappop(pq)
            visited.add(node)
            for weight, child in adjList[node]:
                if child in visited:
                    continue
                if weight > minTime[child]:
                    continue
                minTime[child] = min(minTime[child], minval+weight)
                heapq.heappush(pq, [minTime[child],child])

        
        maxTime = max(minTime.values())
        if maxTime == float('inf'):
            return -1
        else:
            return maxTime


            




        

        


        

        

        

        


        