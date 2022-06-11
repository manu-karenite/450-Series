#https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s)>k:
            temp=[]
            #dividing now
            for z in range(0,len(s),k):
                temp.append(s[z:z+k])
            print(temp)
            #temp is now an array
            st=""
            for x in temp:
                y=list(x)
                y=[int(z) for z in y]
                y=str(sum(y))
                st=st+y
            s=st
            print(st)

        return(s)
                
        