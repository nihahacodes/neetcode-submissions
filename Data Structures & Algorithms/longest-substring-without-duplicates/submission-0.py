class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxlen=0
        hash={}
        while r<len(s):
            if s[r] in hash:
                if hash[s[r]]>=l:
                    l=hash[s[r]]+1
            maxlen=max(maxlen,r-l+1)
            hash[s[r]]=r
            r+=1
        return maxlen