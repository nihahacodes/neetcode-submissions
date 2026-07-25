class Solution:

    def encode(self, strs):
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s):
        ans = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#' after the length
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            # Read EXACTLY 'length' characters
            word = s[j+1 : j+1+length]
            ans.append(word)

            # Move to the next encoded string
            i = j + 1 + length

        return ans
