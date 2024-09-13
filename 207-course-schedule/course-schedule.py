from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMat = defaultdict(list)
        for course1, course2 in prerequisites:
            adjMat[course1].append(course2)


        def dfs(course):
            if adjMat[course] == []:
                return True
            if course in visited:
                return False

            visited.add(course)
            for c in adjMat[course]:
                if dfs(c) == False:
                    return False

            adjMat[course] = []
            return True

        visited = set()

        for courses in range(numCourses):
            if courses not in visited:
                if dfs(courses) == False:
                    return False

        return True

            

        