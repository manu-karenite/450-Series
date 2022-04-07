class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> full;
        
        for(int i=0;i<nums1.size();i++){
            full.push_back(nums1[i]);
        }
        for(int i=0;i<nums2.size();i++){
            full.push_back(nums2[i]);
        }
        sort(full.begin(),full.end());
        if((nums1.size()+nums2.size())%2==1){
            //odd shaped
            return full[(nums1.size()+nums2.size())/2];
        }else{
            return (full[full.size()/2]+full[full.size()/2-1])/2.0;
        }
    }
};