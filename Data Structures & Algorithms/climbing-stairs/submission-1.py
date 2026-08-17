class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        left=self.climbStairs(n-1)
        right=self.climbStairs(n-2)
        return left+right