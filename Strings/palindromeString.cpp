class Solution{
public:	
	
	
	int isPalindrome(string S)
	{
	    int i=0;
	    int j=S.size()-1;
	    while(i<=j){
	        if(S[i]!=S[j])return false;
	        i++;
	        j--;
	    }
	    return true;
	}

};