# https://leetcode.com/problems/shortest-distance-to-a-character/

from math import fabs


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []

        idx = 0
        for x in s:
            if x == c:
                ans.append(0)
            else:
                # we ave different character
                left = s[0:idx]
                right = s[idx+1:]

                left = left[::-1]  # reverse

                l = 2**31
                r = 2**31
                if c in left:
                    l = left.index(c)
                if c in right:
                    r = right.index(c)
                r = idx+r+1
                l = idx-l-1

                val = min(fabs(idx-l), fabs(idx-r))
                ans.append(int(val))
            idx = idx+1

        return ans
