#https://leetcode.com/problems/replace-words/

class Solution:
    def solve(self,dic,word):
        for x in dic:
            if x in word and word.index(x)==0:
                return x
        return word
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        lis=[]
        s=sentence.split(" ")
        for x in s:
            word=self.solve(dictionary,x)
            print(word)
            lis.append(word)
        return " ".join(lis)
        