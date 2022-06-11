#https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dishes=set()
        d={} #key->table number
        for x in orders:
            food=x[2]
            table=x[1]
            dishes.add(food)
            if table in d:
                foodlist=d[table]
                if food in foodlist:
                    #curr_food=foodlist[food]
                    foodlist[food]+=1
                else:
                    #curr_food=foodlist[food]
                    foodlist[food]=1
                
                
            else:
                #create a new entry for table
                d1={}
                d1[food]=1
                d[table]=d1
        print(d)
        
        #now the menu is created
        
        lis=list(dishes)
        leng=len(lis)
        lis.sort()

        indices={}
        for i,x in enumerate(lis):
            indices[x]=i+1
        print(indices)
            

        lis.insert(0,"Table")
        print(lis)
        fin=[]
        for x in d:
            t=["0"]*leng
            t.insert(0,x)

            foodlist=d[x]
            
            
            #we have foodist as internal dictionary
            for key in foodlist:
                idx=indices[key]
                t[idx]=str(foodlist[key])
            
            fin.append(t)
        print(fin)
        fin.sort(key=lambda x:int(x[0]))
        print(fin)
        fin.insert(0,lis)
        return(fin)
            