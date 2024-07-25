class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        adjMat = defaultdict()
        numOfRooms = len(rooms)
        for i in range(numOfRooms):
            adjMat[i] = rooms[i]
        '''

        def dfs(node):
            if node in visited:
                return 
            if node == []:
                return

            visited.add(node)
            for child in rooms[node]:
                dfs(child)


        visited = set()
        dfs(0)
        if len(visited) == len(rooms):
            return True
        return False

            

        
        