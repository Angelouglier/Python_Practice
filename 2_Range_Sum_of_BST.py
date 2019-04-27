# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        if root.val >= L:
            if root.val <= R:
                count += root.val
        if root.left != None:
            count += self.rangeSumBST(root.left, L, R)
        if root.right != None:
            count += self.rangeSumBST(root.right, L, R)
        return count
