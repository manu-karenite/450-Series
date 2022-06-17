#https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        d={}
        lis=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for i in range(0,12,1):
            d[lis[i]]=i+1
        print(d)
        
        arr=date.split(" ")
        date,month,year=arr[0],arr[1],arr[2]
        
        date=date[::-1]
        date=date[2:]
        date=date[::-1]
        print(date)
        if len(date)==1:
            date="0"+date
        n=str(d[month])
        if len(n)<2:
            n="0"+n
        s=year+"-"+n+"-"+date
        return s