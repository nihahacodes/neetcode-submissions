class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp={}
        for num in nums:
            if num not in mpp:
                mpp[num]=1
            else:
                mpp[num]+=1
        mpp=dict(sorted(mpp.items()))
        print(mpp)
        return list(mpp.keys())[-k:]
