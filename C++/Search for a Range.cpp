
/*
Search for a Range 
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
前后指针向中间逼近

*/
class Solution {
public:
    vector<int> searchRange(int A[], int n, int target) {
        vector<int> res;
        int start = 0, end = n-1;
        for(;A[start]!=target&&start<n;start++){
            ;
        }
        
        if(start == n){
            res.push_back(-1);
            res.push_back(-1);
            return res;
        }
        
        for(;A[end]!=target;end--){
            ;
        }
        
        res.push_back(start);
        res.push_back(end);
        return res;
       
    }
};