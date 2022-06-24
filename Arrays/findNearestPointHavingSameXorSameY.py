#https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

from math import fabs
class Solution:
    
    def manhattan(self,x1,y1,x2,y2):
        ans=int(fabs(x1-x2))+int(fabs(y2-y1))
        return ans
        
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        
        d={}
        maxi=2**31-1
        for i,m in enumerate(points):
            if m[0]==x or m[1]==y:
                #go ahead
                ans=self.manhattan(m[0],m[1],x,y)
                maxi=min(maxi,ans)
                if ans in d:
                    temp=d[ans]
                    temp.append(i)
                    d[ans]=temp
                    
                else:
                    d[ans]=[i]
                    
            
        
        if maxi==2**31-1:
            return -1
        else:
            return min(d[maxi])