#https://leetcode.com/problems/shortest-completing-word/

class Solution:
    def byLength(self,word):
        return len(word)
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        words.sort(reverse=False,key=self.byLength)
        allowed={}
        
        #create a dictionary of all license letters
        for x in licensePlate:
            x=x.lower()
            if x.isalpha()==True:
                if x in allowed:
                    allowed[x]=allowed[x]+1
                else:
                    allowed[x]=1
        checked=set()
        print(allowed)
        for word in words:
            flag=True
            #for checking each word
            for y in allowed:
                count=word.count(y)
                print(y,count,allowed[y])
                if count>=allowed[y]:
                    continue
                else:
                    flag=False
                    break
            
            if flag==False:
                continue
            else:
                return word
            
            
            
            
                