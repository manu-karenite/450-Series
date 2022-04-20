#https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        #just one is required to increment
        leng=len(digits)
        last = len(digits)-1
        #get the curr digit
        curr=digits[last]
        
        #increment it
        curr=curr+1+carry
        digits[last]=curr%10
        carry=curr//10
        
        if leng==1:
             if carry!=0:
                digits.insert(0,carry)
                
        else:
            #when atleast two digits
            j=last-1
            while j>=0:
                if j==0:
                    curr=digits[j]+carry
                    digits[j]=curr%10
                    carry=curr//10
                    if carry!=0:
                        digits.insert(0,carry)
                    break
                else:
                    curr=digits[j]+carry
                    digits[j]=curr%10
                    carry=curr//10
                    j=j-1
        
        return digits
            
        
        