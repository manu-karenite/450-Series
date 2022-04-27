#https://leetcode.com/problems/count-the-number-of-consistent-strings/
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        all=set()
        
        for y in allowed:
            all.add(y)  
        orig=len(all)
        for x in words:
            temp=set()
            for y in x:
                temp.add(y)
            print(temp)
            
            diff=all.union(temp)
            print(diff)
            if len(diff)==orig:
                count=count+1
        return count
            