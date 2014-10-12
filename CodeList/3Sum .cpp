/*
3Sum 

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
*/

class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
        
        vector<vector<int>> result;
        if (num.size() < 3) return result;
          sort(num.begin(), num.end());
          
          auto last=num.end();
          
          for(auto a = num.begin(); a < prev(last, 2);a = upper_bound(a, prev(last, 2), *a))
              for(auto b = next(a); b < prev(last);b = upper_bound(b, prev(last), *b)){
                  int target = 0 - *a - *b;
                  if (binary_search(next(b), last, target))
                      result.push_back(vector<int> {*a, *b, target});

                //   for(int k=j+1;k<num.size();k++)
                //     if(num[k]==target){
                //       result.push_back(vector<int> {num[i],num[j],target });
                //       break; 
                //     }   //这么暴力的超时了
                
                
            }
          
        return result;
    }
};