#https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def bySum(self,arr):
        return arr[1]
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        leng1=len(list1)
        leng2=len(list2)
        
        small=[]
        large=[]
        if leng1<leng2:
            small=list1
            large=list2
        else:
            small=list2
            large=list1
            
        common=[]
        #decided the list now
        for x in small:
            
            if x in large:
                
                ans=[x,small.index(x)+large.index(x)]
                common.append(ans)
        print(common)
        
        common.sort(key=self.bySum)
        #since an answer always exists
        mincharge=common[0][1]
        ans=common[0][0]
        i=1
        while i<len(common):
            if common[i][1]>mincharge:
                break
            i=i+1
        #we break at i
        
        common=common[0:i]
        print(common)
        
        lis=[]
        for x in common:
            lis.append(x[0])
        print(lis)
        return lis
                
            
            