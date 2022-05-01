#https://leetcode.com/problems/count-common-words-with-one-occurrence/submissions/

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        m={}
        for x in words1:
            if x in m:
                m[x]=m[x]+1
            else:
                m[x]=1
        n={}
        for x in words2:
            if x in n:
                n[x]=n[x]+1
            else:
                n[x]=1
        
        count=0
        for z in m:
            if z in n:
                if m[z]==1 and n[z]==1:
                    count=count+1
        return count
                