class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robline(arr):
            if len(arr)==1:
                return arr[0]
            dp=[0]*len(arr)
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            for i in range(2,len(arr)):
                dp[i]=max(dp[i-1],dp[i-2]+arr[i])
            return dp[-1]
        case1=robline(nums[1:])
        case2=robline(nums[:-1])
        return max(case1,case2)
        