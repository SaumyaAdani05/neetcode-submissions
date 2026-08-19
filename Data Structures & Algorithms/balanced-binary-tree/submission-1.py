class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root):
            nonlocal balanced
            if root is None:
                return 0
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            if abs(left - right) > 1:
                balanced = False
            return max(left, right)
        dfs(root)
        return balanced