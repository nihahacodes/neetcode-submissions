class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for curr in range(1,amount+1):
            for coin in coins:
                if curr>=amount:
                    dp[curr]=min(dp[amount-curr]+1,dp[curr])
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]