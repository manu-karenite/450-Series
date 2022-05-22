#https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range (1,num+1,1):
            sum=0
            x=i
            while x>0:
                sum=sum+x%10
                x=x//10
            if sum%2==0:
                count+=1
        return count
        