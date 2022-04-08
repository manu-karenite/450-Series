#include <bits/stdc++.h>
class Solution {
public:
bool getChecked(int num){
    stack<int> st;
    queue<int> q;
    
    while(num>0){
        int x = num%10;
        st.push(x);
        q.push(x);
        num=num/10;
    }
    
    while(q.size()!=0){
        if(st.top()!=q.front()){
            return false;
        }
        st.pop();
        q.pop();
    }
    return true;
}
    int PalinArray(int a[], int n)
    {
    	for(int i=0;i<n;i++){
    	    bool ans=getChecked(a[i]);
    	    if(ans==false){
    	        return 0;
    	    }
    	}
    	return true;
    }
};
