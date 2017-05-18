/*Subsets
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

妈的网上和教材里说的每一个对的，数位法要纸上画一下后再做，就会比较明白到底怎么回事
*/

class Solution {

public:
    vector<vector<int> > subsets(vector<int> &S) {
          sort(S.begin(), S.end()); //输出有序
          vector<vector<int> > res;
          long n = pow(2,S.size());//总共有n种情况
          
          for(long i=0;i<n;i++){
              vector<int> v;
              for(int j=0;j<S.size();j++){
                  if((1<<j)&i){
                      v.push_back(S[j]);
                  }     
              }
              
              res.push_back(v);
              v.clear();    
          }
          
          return res;
         
    }
};