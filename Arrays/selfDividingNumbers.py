# https://leetcode.com/problems/self-dividing-numbers/

class Solution:

    def check(self, n: int) -> bool:
        temp = n
        while n > 0:
            rem = n % 10
            n = n//10
            if rem == 0:
                return False
            if temp % rem != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        ans = []
        for x in range(left, right+1, 1):
            val = self.check(x)
            if val == True:
                ans.append(x)
        return(ans)
