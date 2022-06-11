#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x=[[1]]
        if numRows==1:
            return x
        
        
        for i in range(1,numRows):
            prev=x[i-1]
            temp=[prev[0]]
            for j,y in enumerate(prev[1:]):
                temp.append(y+prev[j])
            temp.append(prev[-1])
            x.append(temp)
        return(x)
        