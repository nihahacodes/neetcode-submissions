class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')

        def nodesum(node):
            if node is None:
                return 0

            lsum = max(0, nodesum(node.left))
            rsum = max(0, nodesum(node.right))

            self.maxi = max(self.maxi, node.val + lsum + rsum)

            return node.val + max(lsum, rsum)

        nodesum(root)
        return self.maxi

