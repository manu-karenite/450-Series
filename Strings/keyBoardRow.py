#https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        rows=[row1,row2,row3]
        ans=[]
        
        for x in words:
            #we have min length as 1
            #get the 1st character
            print(x)
            z=x.lower()
            letter=z[0:1]
            init_row=-1
            if letter in rows[0]:
                init_row=0
            elif letter in rows[1]:
                init_row=1
            else:
                init_row=2
            flag=True
            for y in range(1,len(z)):
                letter=z[y]
                if letter not in rows[init_row]:
                    flag=False
                    break
                else:
                    continue
            
            if flag==True:

                ans.append(x)
                

        return ans
            
            
        