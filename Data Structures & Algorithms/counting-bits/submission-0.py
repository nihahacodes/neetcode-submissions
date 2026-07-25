class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            c = 0
            num = i

            while num:
                num &= (num - 1)   # removes the rightmost set bit
                c += 1

            ans.append(c)

        return ans