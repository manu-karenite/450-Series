# https://leetcode.com/problems/number-of-days-between-two-dates/

from datetime import date


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        [x1, y1, z1] = date1.split("-")
        # d1=date(intx1,y1,z1)
        d1 = date(int(x1), int(y1), int(z1))
        [x1, y1, z1] = date2.split("-")
        d2 = date(int(x1), int(y1), int(z1))
        diff = d2-d1
        if d1 > d2:
            diff = d1-d2

        return diff.days
