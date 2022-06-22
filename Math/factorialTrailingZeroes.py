#https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        
        
        
#         10-> 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x9 x 10
#         10-> 1 x 2 x 3 x 2 x 2 x 5 x 2 x 3 x 2 x 2 x 2 x 3 x 3 x 2 x 5
        
#         10-> depends on 2*5 eventually
        
#         20-> 5 , 2x 5 , 5 x 3 5 x 4
        
#         20-> 
        
   # 5, 5 , 5 x 5 x 5 x 5 

#100-> 100//5 -> 20    100//25 ->  4 ,,, 100//125 =0 end
        s=0
        p=1
        while n//(5**p)>0:
            s+=n//(5**p)
            p+=1
        return s
        
        
    
        