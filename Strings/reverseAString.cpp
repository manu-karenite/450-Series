#include <vector>
class Solution {
public:
    void reverseString(vector<char>& s) {
        int len = s.size();
        int i=0;
        int j=len-1;
        while(i<=j){
            char temp = s.at(i);
            s.at(i)=s.at(j);
            s.at(j)=temp;
            i++;
            j--;
        }
    }
};