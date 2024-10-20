class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for node1, node2 in redEdges:
            red[node1].append(node2)

        for node1, node2 in blueEdges:
            blue[node1].append(node2)
        queue = deque([(0, 0, "No")])
        visited = set()
        visited.add((0, None))
        res = [-1]*n
        while queue:

            for i in range(len(queue)):
                node, length, color = queue.popleft()
                if res[node] == -1:
                    res[node] = length
                


                if color != "Red":
                    for child in red[node]:
                        if (child, "Red") in visited:
                            continue
                        queue.append((child, length+1, "Red"))
                        visited.add((child, "Red"))

                if color != "Blue":
                    for child in blue[node]:
                        if (child, "Blue") in visited:
                            continue
                        queue.append((child, length+1, "Blue"))
                        visited.add((child, "Blue"))

        return res


        