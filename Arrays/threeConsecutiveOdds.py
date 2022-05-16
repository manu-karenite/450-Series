# https://leetcode.com/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        lis = []
        for x in arr:
            if x % 2 == 0:  # even
                lis = []

            else:  # odd
                if len(lis) == 2:
                    return True
                else:
                    lis.append(x)

        return False
