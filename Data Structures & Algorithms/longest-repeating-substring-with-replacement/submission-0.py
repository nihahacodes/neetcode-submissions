class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        maxlen=0
        maxf=0
        hash={}
        while r<len(s):
            hash[s[r]] = hash.get(s[r], 0) + 1
            maxf=max(maxf,hash[s[r]])
            while((r-l+1)-maxf>k):
                hash[s[l]]-=1
                maxf=max(hash.values())
                l+=1
            
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen