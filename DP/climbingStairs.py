# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # we will need dp
        lis = [-1, 1, 2]
        if n == 1 or n == 2:
            return lis[n]

        for i in range(3, n+1):
            sum = lis[i-1]+lis[i-2]
            lis.append(sum)
        return lis[n]
