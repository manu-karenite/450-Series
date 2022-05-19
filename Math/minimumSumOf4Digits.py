# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        dig = []
        for x in str(num):
            dig.append(x)
        print(dig)

        dig.sort()
        print(dig)

        one = []
        two = []
        one.append(dig[0])
        one.append(dig[2])
        two.append(dig[1])
        two.append(dig[3])
        print(one, two)

        x = int("".join(one))
        y = int("".join(two))
        return (x+y)
