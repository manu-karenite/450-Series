# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        x = (bin(n)[2:])
        l = x.split("0")
        sum = 0
        for y in l:
            sum = sum+len(y)

        return sum
