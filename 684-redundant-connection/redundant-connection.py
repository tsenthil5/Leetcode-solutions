class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]


        def find(n):
            p = parent[n]
            while p!=parent[p]:
                #parent[p] = parent[parent[p]]
                p = parent[p]

            return p
    

        for edgeStart, edgeEnd in edges:
            pstart, pend = find(edgeStart), find(edgeEnd)
            if pstart == pend:
                return [edgeStart,edgeEnd]

            else:
                if rank[pstart] > rank[pend]:
                    rank[pstart]+=rank[pend]
                    parent[pend] = pstart
                else:
                    rank[pend]+=rank[pstart]
                    parent[pstart] = pend  

        print(parent)
        print(rank)  
                


        

         
        