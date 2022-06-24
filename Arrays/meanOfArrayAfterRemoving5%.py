#https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        count=len(arr)//20
        arr=arr[count:len(arr)-count]
        #print(arr,len(arr))
        return sum(arr)/len(arr)
        
        
        #1 2 3 4 5 6