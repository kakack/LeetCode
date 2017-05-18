/*
Pascal's Triangle II 
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
*/

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        
        vector<int> result;
        long long cur = 1;
        result.push_back(cur);
        

            for(int i=1;i<=rowIndex;i++){
              cur=cur*(rowIndex-i+1)/i;
              
              result.push_back(cur);
              }  

        return result;
        
    }
};