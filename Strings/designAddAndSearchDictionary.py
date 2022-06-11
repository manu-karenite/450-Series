#https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.s=set()
        
        

    def addWord(self, word: str) -> None:
        self.s.add(word)
        

    def search(self, word: str) -> bool:
        #okay
        reqd=len(word)
        if word in self.s:
            return True
        
        if "." not in word and word not in self.s:
            return False
        lis=[]
        for x in self.s:
            
            if len(x)==reqd:
                lis.append(x)
        
        #print(word,lis)
        if not lis:
            return False
        
        #now lis contains some word, jinka dot change karke dekhna padega
        dotsindex=[]
        ct=0
        for i,x in enumerate(word):
            if x==".":
                dotsindex.append(i)
                ct+=1
        #print(dotsindex)
        
        wordlist=list(word)
        
        for x in lis:
            t=list(x)
            if ct==1:
                t[dotsindex[0]]="."
                if t==wordlist:
                    return True
                
            elif ct==2:
                t[dotsindex[0]]="."
                t[dotsindex[1]]="."
                if t==wordlist:
                    return True
                
            elif ct==3:
                t[dotsindex[0]]="."
                t[dotsindex[1]]="."
                t[dotsindex[2]]="."
                if t==wordlist:
                    return True
        return False
        
        

            

                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)