# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:

        p = 0
        num = 0
        s = s[::-1]
        for x in s:
            if x == '0':
                num = num+0
            else:
                num = num+2**p
            p = p+1
        print(num)

        step = 0
        while num != 1:
            if num % 2 == 0:
                num = num//2

            else:
                num = num+1
            step = step+1
        return step
