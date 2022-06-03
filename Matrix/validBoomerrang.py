#https://leetcode.com/problems/valid-boomerang/

from math import gcd
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        #should form a triangle
        x1,y1,x2,y2,x3,y3=points[0][0],points[0][1],points[1][0],points[1][1],points[2][0],points[2][1]
        
        #calculate area
        
        a=((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3))/2
        return a!=0