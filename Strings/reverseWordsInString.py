#https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        ans=s.split(" ")
        print(ans)
        ans=list(filter(lambda x :  x!="",ans))
        print(ans)
        ans=ans[::-1]
        ans=" ".join(ans)
        return ans
        