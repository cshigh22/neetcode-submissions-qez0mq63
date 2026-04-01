# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            left_gain = dfs(root.left)
            right_gain = dfs(root.right)
            left_gain = max(left_gain, 0)
            right_gain = max(right_gain, 0)
            res[0] = max(res[0], root.val + left_gain + right_gain)
            return root.val + max(left_gain, right_gain)
        dfs(root)
        return res[0]
