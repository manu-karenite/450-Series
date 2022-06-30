#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        i=0
        for x in mat:
            #x is list
            soldiers=x.count(1)
            civilians=x.count(0)
           # print(soldiers,civilians)
            ans.append([soldiers,i])
            i+=1
        ans.sort()
        #print(ans)
        fin=[]
        for x in ans[0:k]:
            fin.append(x[1])
        return fin
            