# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def get(self, s):
        # print(s)
        i = 0
        sum = 0
        while i < len(s):
            sum = sum+int(s[i:i+1])
            i = i+1
        # print(sum)
        return str(sum)

    def getLucky(self, s: str, k: int) -> int:

        lis = []
        for x in s:
            diff = ord(x)-96
            # print(diff)
            lis.append(str(diff))
        s = "".join(lis)
        # print(s)

        while k > 0:
            s = self.get(s)

            k = k-1
        return int(s)
