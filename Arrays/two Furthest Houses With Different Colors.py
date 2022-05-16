# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        a = colors[0]
        l = -1
        j = len(colors)-1

        while j > 0:
            if colors[j] == a:
                j = j-1
            else:
                l = j
                break

        # for right
        b = colors[len(colors)-1]
        i = 0
        while i <= len(colors)-2:
            if colors[i] == b:
                i = i+1
            else:
                return max(l, len(colors)-1-i)
