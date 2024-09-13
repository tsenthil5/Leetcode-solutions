"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        visited = {}
        old_to_new

        1) add node to visited
        2) create copy
        3) map old to new
        4) check if prev is None else:
        connect prev -> new
        5) dfs(neibhors, prev)
        '''

        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            newNode = Node(node.val)
            old_to_new[node] = newNode
            for n in node.neighbors:
                newNode.neighbors.append(dfs(n))

            return newNode


        return dfs(node) if node else None
        
        