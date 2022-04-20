#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        leng=len(nums)
        capacity=leng//2
        
        dictionary={}
        
        for x in nums:
            arr=dictionary.keys()
            print(dictionary)
            if x in arr:
                dictionary[x]=dictionary[x]+1
            else:
                dictionary[x]=1
        
        print(dictionary)
        for x in dictionary:
            if dictionary[x]>capacity:
                return x
            