# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # def dfs(node, maxVal):
        #     if not node:
        #         return 0
        #     res = 1 if node.val >= maxVal else 0
        #     maxVal = max(maxVal, node.val)
        #     res += dfs(node.left, maxVal)
        #     res += dfs(node.right, maxVal)
        #     return res
        # return dfs(root, root.val)
        if not root:
            return 0

        q = deque([(root, root.val)])
        res = 0

        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                res += 1
                maxVal = node.val

            if node.left:
                q.append((node.left, maxVal))
            if node.right:
                q.append((node.right, maxVal))
        return res