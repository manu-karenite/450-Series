# https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target != 1:

            if maxDoubles > 0:
                if target % 2 == 0:
                    target = target//2
                    maxDoubles = maxDoubles-1
                    count = count+1

                else:
                    target = target-1
                    count = count+1

            else:
                return count+(target-1)

        return count
