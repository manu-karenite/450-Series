#https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d={}
        for dir in paths:
            #contains folder and path
            b=dir.split(" ")
            folder=b[0]
            b=b[1:]
            for files in b:
                content=files.split("(")
                filename=content[0]
                body=content[1][0:len(content[1])-1]
                print(filename,body)
                if body in d:
                    lis=d[body]
                    lis.append(folder+"/"+filename)
                    d[body]=lis
                else:
                    d[body]=[folder+"/"+filename]
        print(d)
        ans=[]
        for x in d:
            if len(d[x])>1:
                ans.append(d[x])
        return ans
            
        