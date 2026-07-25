class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp={}
        for word in strs:
            key="".join(sorted(word))

            if key not in mpp:
                mpp[key]=[]
            mpp[key].append(word)
        return list(mpp.values())
