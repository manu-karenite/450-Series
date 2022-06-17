#https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        d={}
        for x in edges:
            
            a=x[0]
            b=x[1]
            if a in d:
                d[a]+=1
            else:
                d[a]=1
                
            if b in d:
                d[b]+=1
            else:
                d[b]=1
        print(d)
        
        z=len(edges)
        
        for x in d:
            if d[x]==z:
                return x
            
            
            
        