# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs(node, depth):
        #     if not node:
        #         return 
        #     if depth == len(res):
        #         res.append(node.val)
        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)
        
        # dfs(root, 0)
        # return res
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()

                if i == level_length - 1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
