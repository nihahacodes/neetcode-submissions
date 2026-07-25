class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp={}
        for num in nums:
            if num not in mpp:
                mpp[num]=1
            else:
                mpp[num]+=1
        
        sorted_items = sorted(mpp.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for key, value in sorted_items[:k]:
            ans.append(key)

        return ans
