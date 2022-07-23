#https://practice.geeksforgeeks.org/problems/number-of-ways2552/1

#User function Template for python3

class Solution:
    def arrangeTiles(self, N):
        # code here
        if N<=3:
            return 1
        
        # return self.arrangeTiles(N-1)+self.arrangeTiles(N-4)
        
        #SOLVE BY DP
        temp=[]
        for i in range(0,N+1):
            temp.append(0)
        
        temp[0]=temp[1]=temp[2]=temp[3]=1
        for i in range(4,N+1):
            temp[i]=temp[i-4]+temp[i-1]
        return temp[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.arrangeTiles(N))

# } Driver Code Ends