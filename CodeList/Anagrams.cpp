/*Anagrams
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.

Anagrams回文构词法只是改变了单词顺序，没有改变数目，所以如果属于同一个Anagrams那么他们sort一下后的结果是一样的。
*/

class Solution {
public:
    vector<string> anagrams(vector<string> &strs) {
        map<string,int> anagrams;
        vector<string> result;
        string s;
        
        for(int i=0;i<strs.size();i++){
            s=strs[i];
            
            sort(s.begin(),s.end());
            
            if(anagrams.find(s)==anagrams.end())//没找到
              anagrams[s]=i;
              
            else{//已经有了
            if(anagrams[s]>=0)
              {
                  result.push_back(strs[anagrams[s]]);
                  anagrams[s]=-1;//这是为了防止重复一样的字串
              }
                result.push_back(strs[i]);
            }
            
            
        }
        
        return result;
        
    }
};