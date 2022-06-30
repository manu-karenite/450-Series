#https://leetcode.com/problems/k-th-smallest-prime-fraction/

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(0,len(arr)-1,1):
            for j in range(i+1,len(arr),1):
                ans.append([arr[i]/arr[j],[arr[i],arr[j]]])
        #print(ans)
        ans.sort()
        return ans[k-1][1]
        