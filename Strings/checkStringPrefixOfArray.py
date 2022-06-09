#https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for x in words:
            if s=="":
                return True
            if x in s:
                idx=s.index(x)
                print(s,idx,x)
                if idx!=0:
                    return False
                new_index=idx+len(x)
                s=s[new_index:]
                
                
            else:
                return False
            
        if s!="":
            return False
        return True
        