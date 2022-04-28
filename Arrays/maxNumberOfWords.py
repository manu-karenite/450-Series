#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=-1
        for i,item in enumerate(sentences):
            #item is the sentence
            x=item.split()
            if len(x)>ans:
                ans=len(x)
        return ans
        