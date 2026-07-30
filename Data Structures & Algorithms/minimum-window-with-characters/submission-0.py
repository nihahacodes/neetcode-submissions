class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash={}
        l=0
        r=0
        minlen=float('inf')
        cnt=0
        sindex=-1
        for ch in t:
            hash[ch] = hash.get(ch, 0) + 1
        while r<len(s):
            if hash.get(s[r],0)>0:
                cnt+=1
            hash[s[r]]=hash.get(s[r],0)-1
            while(cnt==len(t)):
                if(r-l+1<minlen):
                    minlen=min(minlen,r-l+1)
                    sindex=l
                hash[s[l]]+=1
                if hash[s[l]]>0:
                    cnt=cnt-1
                l+=1
            r+=1
        if sindex==-1:
            return ""
        return s[sindex:sindex+ minlen]

