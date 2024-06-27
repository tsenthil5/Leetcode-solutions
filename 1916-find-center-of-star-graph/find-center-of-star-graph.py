from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjMat = defaultdict(list)
        for u,v in edges:
            adjMat[u].append(v)
            adjMat[v].append(u)

        for key, values in adjMat.items():
            if len(values) == len(edges):
                return key



        

        