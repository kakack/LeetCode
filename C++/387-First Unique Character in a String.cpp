/*
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
*/

#include "string"
#include "unordered_map"

using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<int, int> frequency;
        for(auto c: s){
            frequency[c] ++;
        }
        for (int i = 0; i < s.size(); i ++){
            if(frequency[s[i]] == 1){
                return i;
            }
        }
        return -1;
    }
};