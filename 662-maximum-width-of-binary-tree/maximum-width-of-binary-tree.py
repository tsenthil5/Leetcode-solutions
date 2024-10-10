from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Use a deque to store pairs of (node, index)
        queue = deque([(root, 0)])
        maxWidth = 0
        
        while queue:
            level_length = len(queue)
            _, first_node = queue[0]  # Get the index of the first node at this level
            for i in range(level_length):
                node, index = queue.popleft()
                
                # Add child nodes to the queue with updated indices
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            
            # Calculate the width of this level
                if i == level_length-1:
                    last_node = index
            maxWidth = max(maxWidth, last_node - first_node + 1)
        
        return maxWidth
