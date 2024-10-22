# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findNode(root, parent):
            if not root:
                return None

            if root.val == key:
                return (root, parent)

            if key < root.val:
                return findNode(root.left, root)

            if key > root.val:
                return findNode(root.right, root)

        def delZeroChild(target, parent):
            if target == root:
                return None
            else:
                if parent.left == target:
                    parent.left = None
                if parent.right == target:
                    parent.right = None
                return root

        def delOneChild(target, parent):
            if target == root:
                if target.left:
                    return target.left
                elif target.right:
                    return target.right
            else:
                if parent.left == target:
                    if target.left:
                        parent.left = target.left
                    else:
                        parent.left = target.right
                else:
                    if target.left:
                        parent.right = target.left
                    else:
                        parent.right = target.right

            return root


        def delTwoChild(target, parent):
            # Corrected recursive function to find the inorder successor
            def findInorderSucc(node, parent):
                # The inorder successor is the leftmost node in the right subtree.
                if not node.left:
                    return node, parent  # Return successor and its parent.

                # Recur to find the leftmost node.
                return findInorderSucc(node.left, node)

            # Find the inorder successor and its parent.
            inOrdChild, inOrdPar = findInorderSucc(target.right, target)

            # Replace target's value with the successor's value.
            target.val = inOrdChild.val

            # Update the parent's pointer to remove the inorder successor.
            if inOrdPar.left == inOrdChild:
                inOrdPar.left = inOrdChild.right
            else:
                inOrdPar.right = inOrdChild.right

            return root

        target = findNode(root, root)
        if not target:
            return root

        else:
            target, parent = target[0], target[1]

        if not target.left and not target.right:
            return delZeroChild(target, parent)

        elif target.left and not target.right or target.right and not target.left:
            return delOneChild(target, parent)

        elif target.left and target.right:
            return delTwoChild(target, parent)

        
        

        

         
        