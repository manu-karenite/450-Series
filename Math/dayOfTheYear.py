#https://leetcode.com/problems/day-of-the-year/

class Solution:
    
    def answerLeapYear(self,year):
        #return True or False
        if year%400==0 and year%100==0:
            return True
        
        elif year%4==0 and year%100!=0:
            return True
        return False
        
    def findDay(self,date,month,dic):
        #let month be x
        previousMonth=month-1
        s=0
        for i in range(1,previousMonth+1,1):
            s+=dic[i]
        s+=date
        return s
            
    def dayOfYear(self, date: str) -> int:
        
        d={}
        d[1]=31
        d[3]=31
        d[4]=30
        d[5]=31
        d[6]=30
        d[7]=31
        d[8]=31
        d[9]=30
        d[10]=31
        d[11]=30
        d[12]=31
        s,month,dd=date.split("-")[0],int(date.split("-")[1]),int(date.split("-")[2])
        
        s=int(s)
        leap=self.answerLeapYear(s)
        if leap:
            d[2]=29
        else:
            d[2]=28
        
        
        return self.findDay(dd,month,d)
    
        
        