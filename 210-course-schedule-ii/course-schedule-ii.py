class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMat = defaultdict(list)
        output = []
        is_source = set()
        for i in range(numCourses):
            is_source.add(i)
        for child, par in prerequisites:
            adjMat[par].append(child)
            if child in is_source:
                is_source.remove(child)


        def topo(node):
            if node in cycle:
                return False
            if node in visited:
                return True

            cycle.add(node)
            for child in adjMat[node]:
                if topo(child) == False:
                    return False

            cycle.remove(node)
            visited.add(node)
            output.append(node)
            return True


        cycle, visited = set(), set()
        for i in range(numCourses):
            if i in is_source:
                if topo(i) == False:
                    return []

        if len(visited) == numCourses:
            output.reverse()

            return output
        else:
            return [] 

        

        