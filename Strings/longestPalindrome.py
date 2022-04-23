#https://leetcode.com/problems/longest-palindrome/submissions/

class Solution:
    def freq(self,num):
        return num[1]
    def longestPalindrome(self, s: str) -> int:
        print(len(s))
        checked=set()
        odd=[]
        summ=0
        maxi=0
        for x in s:
            if x not in checked:
                ct=s.count(x)
                print(x,ct)
                if ct%2==0:
                    summ=summ+ct
                else:
                    odd.append([x,ct])
            checked.add(x)
        odd.sort(reverse=True,key=self.freq)
        print(odd)
        if len(odd)>0:
            #add the first to summ
            summ=summ+odd[0][1]
            
            #remove from here
            odd=odd[1:len(odd)]
            
            for x in odd:
                summ=summ+x[1]-1
        
        return summ
                
        
