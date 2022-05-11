# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for lis in grid:
            for x in lis:
                if x < 0:
                    count = count+1
        return count
