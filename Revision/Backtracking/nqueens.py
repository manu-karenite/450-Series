class NQueens:
    def __init__(self,n):
        self.n=n
    def printMatrix(self):
        for x in self.temp:
            for y in x:
                print(y,end=" ")
            print(end="\n")
    
    def checkVerticalUp(self,i,j):
        # 0 se i-1 tak check karo in same column
        for i1 in range(0,i):
            if self.temp[i1][j]==1:
                return False
            
        return True

    def checkDiagonalLeft(self,i,j):
        r=i-1
        c=j-1
        while r>=0 and c>=0:
            if self.temp[r][c]==1:
                return False
            r-=1
            c-=1
        return True

        
    def checkDiagonalRight(self,i,j):
        r=i-1
        c=j+1
        while r>=0 and c<self.n:
            if self.temp[r][c]==1:
                return False
            r-=1
            c+=1
        return True



    def checkDirections(self,i,j):
        p=self.checkVerticalUp(i,j)
        
        q=self.checkDiagonalLeft(i,j)
        
        r=self.checkDiagonalRight(i,j)

        return p and q and r
    def nqueens(self,i):
        #\print(i,self.temp)
        if i==self.n:
           
            self.printMatrix()
            #print("------------------------------------")
            return True

        #otherwise,
        #row is i
        #iterate over columns
        for j in range(0,self.n):
            #j is column number... 
            #lets assume now, ki arr[i][j] pe rakh diye hain
            ans=self.checkDirections(i,j)
            if ans:
                self.temp[i][j]=1
                #now check wheter its okay to keep or not...
                whatnext=self.nqueens(i+1) #work on next row NOW
                if whatnext:
                    return True
                self.temp[i][j]=0
        return False




    
    
    def initialiseMatrix(self):
        self.temp=[]
        for i in range(0,self.n):
            self.temp.append([0]*self.n)
        #now solve the matrix

        ans=self.nqueens(0)
        if ans:
            print("Possible")
        else:
            print("Not Possible !")
        
        

def main():
    n=int(input("Enter the Value of n for N-Queens : "))
    obj=NQueens(n)
    obj.initialiseMatrix()
    #obj.printMatrix()
if __name__ =="__main__":
    main()