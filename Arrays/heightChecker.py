# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = []
        for x in heights:
            target.append(x)

        target.sort()

        count = 0

        for i, x in enumerate(heights):
            if x != target[i]:
                count = count+1
        return count
