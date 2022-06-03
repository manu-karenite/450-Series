#https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans=[]
        for x in queries:
            count=0
            x,y,r=x[0],x[1],x[2]
            for z in points:
                p=z[0]
                q=z[1]
                #check the equations
                #(p-x)^2 + (q-y)^2 - r^2<=0
                ans1=(p-x)**2 + (q-y)**2 - r**2
                if ans1<=0:
                    count+=1
                
            ans.append(count)
        return ans
            
        
        