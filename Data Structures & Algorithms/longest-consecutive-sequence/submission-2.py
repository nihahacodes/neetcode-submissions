class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lastsmaller=float('inf')
        longest=0
        count=0
        nums.sort()
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i]-1==lastsmaller:
                lastsmaller=nums[i]
                count+=1
            else:
                lastsmaller=nums[i]
                count=1
            longest=max(longest,count)
        return longest+1