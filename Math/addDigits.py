# https://leetcode.com/problems/add-digits/

class Solution:

    def ans(self, num: int) -> int:

        ans = 0
        while num > 0:
            ans = ans+num % 10
            num = num//10
        return ans

    def addDigits(self, num: int) -> int:

        while num > 9:
            num = self.ans(num)
        return num
