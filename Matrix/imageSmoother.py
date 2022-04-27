#https://leetcode.com/problems/image-smoother/
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans=[]
        for x in (img):
            ans.append([])
        i=0
        
        rowmax=len(img)
        while i<len(img):
            row=i
            j=0
            while j<len(img[i]):
                x=0
                colmax=len(img[i])
                
                col=j
                sum=img[i][j]
                x=x+1
                
                if col<colmax-1:
                    sum=sum+img[row][col+1]
                    x=x+1
                if col<colmax-1 and row<rowmax-1:
                    sum=sum+img[row+1][col+1]
                    x=x+1
                if col<colmax-1 and row>0:
                    sum=sum+img[row-1][col+1]
                    x=x+1
                    
                if row<rowmax-1:
                    sum=sum+img[row+1][col]
                    x=x+1
                if row>0:
                    sum=sum+img[row-1][col]
                    x=x+1
                
                if col>0:
                    sum=sum+img[row][col-1]
                    x=x+1
                if col>0 and row<rowmax-1:
                    sum=sum+img[row+1][col-1]
                    x=x+1
                if col>0 and row>0:
                    sum=sum+img[row-1][col-1]
                    x=x+1
                
                ans[row].append(int(sum/x))
                j=j+1
            i=i+1
                
                    
        return ans        
                    
                
                
                
                
        