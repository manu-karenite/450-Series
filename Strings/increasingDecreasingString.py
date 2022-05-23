#https://leetcode.com/problems/increasing-decreasing-string/

class Solution:
    def getOne(self,x):
        return x[0]
    def sortString(self, s: str) -> str:
        d={}
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        
        lis=[]
        for x in d:
            lis.append([x,d[x]])        
        lis.sort(key=self.getOne)
        #print(lis)
        
        s=""
        i=0
        z=len(lis)
        
        inc=True
        while len(lis)>0:
            if inc==True:
                i=0
                while i<len(lis):
                    #print(s,lis[i],i)
                    s=s+lis[i][0]
                    freq=lis[i][1]
                    freq-=1
                    if freq==0:
                        lis.remove(lis[i])
                        

                    else:
                        lis[i][1]=freq

                        i+=1
                inc=False
                if inc==False:
                    last=len(lis)-1
                    while last>=0:
                        #print(s)
                        s=s+lis[last][0]
                        freq=lis[last][1]
                        freq-=1
                        if freq==0:
                            lis.remove(lis[last])

                        else:
                            lis[last][1]=freq

                        last-=1
                inc=True
                        
                
        #print(s,lis)
        return s
                
            
        