#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #get the word, with shortest length
        strs.sort(key=len)
        print(strs)
        
        i=0
        ct=0
        while i<len(strs[0]):
            
            s=set()
            j=0
            while j<len(strs):
                s.add(strs[j][i:i+1])
                #print(s,strs[i],strs[j])
                if len(s)>1:
                    #print(s,strs[i],strs[j])
                    return strs[0][:ct]
                
                j+=1
            ct+=1
            i+=1
            
        return strs[0][:ct]
            
        
        