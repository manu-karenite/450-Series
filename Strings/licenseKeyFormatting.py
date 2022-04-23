#https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        split1=s.split("-")
        print(split1)
        split1="".join(split1)
        print(split1)
        
        i=0
        
        while i<len(split1):
            x=split1[i]
            if x.isalpha()==True:
                asci=ord(x)
                if asci>=97 and asci<=122:
                    #lower
                    asci=asci-32
                    letter=chr(asci)
                    split1=split1[0:i]+letter+split1[i+1:]
            i=i+1
        print(split1)
        split1=split1[::-1]
        
        print(split1)
        
        split1=[split1[i:i+k] for i in range(0,len(split1),k)]
        print(split1)
        split1="-".join(split1)
        return split1[::-1]
        