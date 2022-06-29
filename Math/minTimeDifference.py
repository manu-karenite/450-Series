#https://leetcode.com/problems/minimum-time-difference/

from math import fabs
class Solution:
    def findMinDifference(self, tp: List[str]) -> int:
        MAX=1440
        mins=[]
        for x in tp:
            
            h,m=int(x.split(":")[0]),int(x.split(":")[1])
            mins.append(h*60+m)
       
        mins.sort()
                
        ret=2**31-1
        i=0
        while i<len(mins)-1:
            ret=min(ret,int(fabs(mins[i+1]-mins[i])))
            i+=1
            
        #check for the last and first
        ret=min((1440-mins[-1]+mins[0]),ret)
        
        return ret
        
