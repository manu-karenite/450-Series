#https://leetcode.com/problems/day-of-the-week/

from datetime import datetime 
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        x=datetime(year,month,day)
        y=x.strftime("%A")
        return(y)
        