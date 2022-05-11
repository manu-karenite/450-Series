# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        up = 0
        down = len(s)
        ans = []
        if s[0] == 'I':
            ans.append(up)
            up = up+1

        else:
            ans.append(down)
            down = down-1

        t = s[1:]
        for y in t:
            if y == 'I':
                ans.append(up)
                up = up+1

            else:
                ans.append(down)
                down = down-1

        if s[-1] == 'I':
            ans.append(up)

        else:
            ans.append(down)
        return ans
