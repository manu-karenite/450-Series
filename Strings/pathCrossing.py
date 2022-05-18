# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:

        x = 0
        y = 0

        s = set()
        s.add((x, y))

        path = path.strip()
        for l in path:
            if l == "N":
                y = y+1
                if (x, y) in s:
                    return True
                s.add((x, y))

            elif l == "E":
                x = x+1
                if (x, y) in s:
                    return True
                s.add((x, y))

            elif l == "S":
                y = y-1
                if (x, y) in s:
                    return True
                s.add((x, y))

            else:
                x = x-1
                if (x, y) in s:
                    return True
                s.add((x, y))

        return False
