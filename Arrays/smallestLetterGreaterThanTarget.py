#https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lett=[]
        for i in range(0,26,1):
            lett.append(0)
        for x in letters:
            lett[ord(x[0:1])-97]=1
        print(lett)
        
        l=target[0:1]
        start=(ord(l)-97+1)%26
        
        while True:
            if lett[start]==1:
                return chr(97+start)
            start=(start+1)%26
        
        
        