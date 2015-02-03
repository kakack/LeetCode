/*
Longest Common Prefix 
Write a function to find the longest common prefix string amongst an array of strings.
*/
//没有必要所有字串都两两比较，只要每个都跟第一个比较找出最短的就行了
class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if(strs.empty()) return "";
        
        for(int id=0;id<strs[0].size();id++)
          for(int i=1;i<strs.size();i++){
              
              if(strs[i][id]!=strs[0][id]) return strs[0].substr(0,id);
          }
          return strs[0];
    }
};