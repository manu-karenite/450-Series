# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        target = 0
        sum = 0
        while sum <= n:
            target = target+1
            count = count+1
            sum = sum+target
        return count-1
