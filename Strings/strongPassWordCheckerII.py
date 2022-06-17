#https://leetcode.com/problems/strong-password-checker-ii/

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        
        lower=False
        upper=False
        digit=False
        special=False
        adjacent=False
        
        #leave last char for now
        for i in range(0,len(password)-1,1):
            cr=password[i:i+1]
            next_cr=password[i+1:i+2]
            
            if cr==next_cr:
                adjacent=True
                break
                
            if cr.islower()==True:
                lower=True
                
            if cr.isupper()==True:
                upper=True
                
            if cr.isnumeric()==True:
                digit=True
                
            if cr in "!@#$%^&*()-+":
                special=True
                
            
        #managing the last char
        if password[-1].islower()==True:
            lower=True
        if password[-1].isupper()==True:
            upper=True
        if password[-1].isnumeric()==True:
            digit=True
        if password[-1]in "!@#$%^&*()-+":
            special=True
            
        return (lower and upper and digit and special and not adjacent)
            
            
            
        