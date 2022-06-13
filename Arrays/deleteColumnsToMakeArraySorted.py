#https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        col=[]
        for i in range(0,len(strs[0]),1):
            s=""
            for j in range(0,len(strs)):
                s+=strs[j][i:i+1]
            col.append(s)
        print(col)
        ct=0
        for x in col:
            l=list(x)
            
            if l!=sorted(l):
                print(l,sorted(l))
                ct+=1
        return ct
