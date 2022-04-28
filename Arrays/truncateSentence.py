#https://leetcode.com/problems/truncate-sentence/submissions/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x=s.split()
        x=x[0:k]
        x=" ".join(x)
        return x
        