from collections import defaultdict
import heapq as hq
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        max_heap = [0]*n

        for u,v in roads:
            max_heap[u]+=1
            max_heap[v]+=1
        
        for index, item in enumerate(max_heap):
            max_heap[index] = (-1*(item), (index))

        hq.heapify(max_heap)

        nodes_to_imp = {}

        while max_heap:
            maxLen, node = hq.heappop(max_heap)
            nodes_to_imp[node] = n
            n-=1

        totalImp = 0
        for u, v in roads:
            totalImp+=nodes_to_imp[u]
            totalImp+=nodes_to_imp[v]

        return totalImp

        '''
        [0,0,0,0,0]
        max_heap = [2, 3, 4, 2, 1]
        max_heap = [(-2,0),(-3,1),(-4,2),(-2,3),(-1,4)]
        nodes_to_imp = {2:5, 1:4, 3:3,2:2,4:1}
        '''


        




        



        