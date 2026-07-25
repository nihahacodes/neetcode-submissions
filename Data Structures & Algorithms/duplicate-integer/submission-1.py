class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mpp=set()
        for num in nums:
            if num in mpp:
                return True
            mpp.add(num)
        return False