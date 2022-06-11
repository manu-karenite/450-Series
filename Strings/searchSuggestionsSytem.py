#https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        ans=[]
        for i in range(0,len(searchWord)):
            x=searchWord[0:i+1]
            #print(x)
            
            found=[]
            for z in products:
                if x in z and z.index(x)==0:
                    found.append(z)
            #print(found)
            if (len(found)<=3):
                found.sort()
                ans.append(found)
            else:
                found.sort()
                ans.append(found[0:3])
        return(ans)
                
            
        