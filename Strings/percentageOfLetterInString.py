#https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution:
    def percentageLetter(self, s: str, k: str) -> int:
        ct=0
        for x in s:
            print(x)
            if x==k:
                print("MATCHED")
                ct+=1
        
        perc=int((ct/len(s))*100)
        return perc
        