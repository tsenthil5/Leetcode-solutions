class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjMat = defaultdict(list)
        par_child = defaultdict(set)
        visited = set()
        output = []

        for par, child in prerequisites:
            adjMat[par].append(child)


        def topo(node):
            if adjMat[node] == []:
                return []

            if node in visited:
                return par_child[node]

            visited.add(node)
            for child in adjMat[node]:
                
                par_child[node].update(topo(child))
                par_child[node].add(child)

            return par_child[node]


        for parent in list(adjMat.keys()):
            if parent not in visited:
                topo(parent)

        for par, child in queries:
            if child in par_child[par]:
                output.append(True)
            else:
                output.append(False)

        return output

            
            

        