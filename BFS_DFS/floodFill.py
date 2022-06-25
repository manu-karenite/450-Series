#https://leetcode.com/problems/flood-fill/

class Solution:
    
    def fillAll(self,image,sr,sc,color,m,x1,x2,y1,y2,recom):
        if sr<x1 and sr>x2 or sc<y1 or sc>y2:
            return
        #print(sr,sc)
        
        #in limit
        if m[sr][sc]!="X":
            return
        
        if image[sr][sc]!=recom:
            return
        #otherwise,
        orig=image[sr][sc]
        m[sr][sc]=color
        
        if sr-1>=x1:
            self.fillAll(image,sr-1,sc,color,m,x1,x2,y1,y2,orig)
        #print(m)
        if sr+1<=x2:
            self.fillAll(image,sr+1,sc,color,m,x1,x2,y1,y2,orig)
        #print(m)
        if sc-1>=y1:
            self.fillAll(image,sr,sc-1,color,m,x1,x2,y1,y2,orig)
        #print(m)
        if sc+1<=y2:
            self.fillAll(image,sr,sc+1,color,m,x1,x2,y1,y2,orig)
        #print(m)
        #print("-----------------------")
        
        
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        x1=0
        x2=len(image)-1
        
        y1=0
        y2=len(image[0])-1
        m=[]
        for i in range(0,len(image),1):
            temp=[]
            for j in range(0,len(image[0])):
                temp.append("X")
                
            m.append(temp)
        #print(m)
        self.fillAll(image,sr,sc,color,m,x1,x2,y1,y2,image[sr][sc])
        #print(image,m)
        
        for i in range(0,x2+1,1):
            for j in range(0,y2+1,1):
                if m[i][j]=="X":
                    m[i][j]=image[i][j]
                    
        return m
        