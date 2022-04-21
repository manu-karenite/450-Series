#https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:
        
        x=s.split(" ")
        print(x)
        ans=[]
        for word in x:
            #the current word is word
            rev=word[::-1]

            ans.append(rev)

        ans=" ".join(ans)
        return ans