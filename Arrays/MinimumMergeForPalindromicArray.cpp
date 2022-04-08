/*

Given a list of non-negative integers, find the minimum number of merge operations to make it a palindrome.

Input : [6, 1, 3, 7]
Output: 1
Explanation: [6, 1, 3, 7] —> Merge 6 and 1 —> [7, 3, 7]

Input : [6, 1, 4, 3, 1, 7]
Output: 2
Explanation: [6, 1, 4, 3, 1, 7] —> Merge 6 and 1 —> [7, 4, 3, 1, 7] —> Merge 3 and 1 —> [7, 4, 4, 7]

Input : [1, 3, 3, 1]
Output: 0
Explanation: The list is already a palindrome

*/

class Solution
{
public:
	int findMin(vector<int> &nums)
	{
		int count =0;
		int i=0;
		int j=nums.size()-1;
		
		while(i<j){
			if(nums[i]==nums[j]){
				i++;j--;
			}else if (nums[i]<nums[j]){
				i++;
				nums[i]=nums[i]+nums[i-1];
				count++;
			}
			else{
				
				j--;count++;
				nums[j]=nums[j]+nums[j+1];
			}
		}
		return count;
		
	}
};
