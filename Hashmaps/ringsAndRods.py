#https://leetcode.com/problems/rings-and-rods/submissions/

class Solution:
    def countPoints(self, rings: str) -> int:
        d={}
        for i in range (0,10,1):
            d[i]=[]
            
        i=0
        while i<len(rings):
            color=rings[i:i+1]
            number=int(rings[i+1:i+2])
            #get the map
            lis=d[number]
            lis.append(color)
            
            i=i+2
        print(d)
        
        count=0
        for x in d:
            lis=d[x]
            if "R" in lis and "G" in lis and "B" in lis:
                count=count+1
            
        return count
        