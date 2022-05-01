#https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        lis=[]
        for x in logs:
            if x=="../":
                if lis:
                    #not empty
                    lis.pop()
                else:
                    pass
                
            elif x=="./":
                pass
            
            else:
                # get the folder name
                folder_name=x[0:len(x)-1]
                lis.append(folder_name)
        return(len(lis))
                
        