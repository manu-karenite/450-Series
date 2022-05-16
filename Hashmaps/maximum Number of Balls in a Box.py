# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution:
    def countBalls(self, lowlimit: int, highlimit: int) -> int:
        dic = {}

        for x in range(lowlimit, highlimit+1, 1):
            y = str(x)
            y = y.strip()
            print(y)
            y = [int(u) for u in y]
            print(y)
            ans = sum(y)

            if ans in dic:
                dic[ans] = dic[ans]+1
            else:
                dic[ans] = 1
        print(dic)

        ans = -1
        for x in dic:
            ans = max(ans, dic[x])
        return ans
