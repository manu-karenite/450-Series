#https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

from math import fabs
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        sum=0
        for i,x in enumerate(seats):
            sum=int(fabs(x-students[i]))+sum
        return sum
        