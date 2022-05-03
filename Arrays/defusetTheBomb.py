#https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
            
        elif k>0:
            new=[]
            for x in code:
                new.append(x)
            
            #we have to perform sum on every element
            i=0
            while i<len(code):
                count=0
                start=(i+1)%len(code)
                end=(i+k)%len(code)
                sum=0
                while count<k:
                    sum=sum+code[start]
                    start=(start+1)%len(code)
                    count=count+1
                new[i]=sum
                i=i+1
            return new
        else:
            new=[]
            for x in code:
                new.append(x)
            
            #we have to perform sum on every element
            i=0
            while i<len(code):
                
                start=(i-1)%len(code)
                end=(i-k)%len(code)
                sum=0
                count=0
                while count<-k:
                    sum=sum+code[start]
                    start=(start-1)%len(code)
                    count=count+1
                new[i]=sum
                i=i+1
            return new
            
            
        