#https://leetcode.com/problems/angle-between-hands-of-a-clock/

from math import fabs
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mins=minutes*6
        print(mins)
        hrs=hour%12+(minutes/60)
        hrs=hrs*30

        print(hrs)
        
        return min(fabs(hrs-mins),360-fabs(hrs-mins))
        