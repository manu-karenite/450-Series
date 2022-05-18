# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for x in paths:
            [s, des] = [x[0], x[1]]
            if s not in d:
                d[s] = 1
            else:
                d[s] = 1

            if des not in d:
                d[des] = 0
        print(d)

        for x in d:
            if d[x] == 0:
                return x
