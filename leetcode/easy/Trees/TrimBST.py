# Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

# Example 1:                      Example 2:
# Input:                          Input:
#      1                               3
#     / \                             / \
#    0   2                           0   4
#                                     \
#    L = 1                             2
#    R = 2                            /
#                                    1
# Output:
#       1                            L = 1
#        \                           R = 3
#         2
#                                 Output:
#                                       3
#                                      /
#                                    2
#                                   /
#                                  1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

        # When node.val > R, we know that the trimmed binary tree must occur to the left of the node
        if root.val < L:
            return self.trimBST(root.right, L, R)

        # when node.val < L, the trimmed binary tree occurs to the right of the node
        elif root.val > R:
            return self.trimBST(root.left, L, R)

        # Otherwise, we will trim both sides of the tree
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
