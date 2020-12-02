/*
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

建立一个字典。其中 key 为 字符 c，value 为其出现的剩余次数。
从左往右遍历字符串，每次遍历到一个字符，其剩余出现次数 - 1.
对于每一个字符，如果其对应的剩余出现次数大于 1，我们可以选择丢弃（也可以选择不丢弃），否则不可以丢弃。
是否丢弃的标准和上面题目类似。如果栈中相邻的元素字典序更大，那么我们选择丢弃相邻的栈中的元素。

*/

#include "vector"
#include "string"
#include "map"
#include <algorithm>

using namespace std;

class Solution {
public:
    string removeDuplicateLetters(string s) {
        vector<char> letters;
        map<char, int> counts;
        for (int i = 0; i < 26; i++){
            counts.insert(pair<char, int>('a' + i, 0));
        }
        for (char c: s){
            counts[c] ++;
        }
        for (char c: s){
            if (find(letters.begin(), letters.end(), c) == letters.end()){
                while (!letters.empty() && c < letters.back() && counts[letters.back()] > 0) {
                    letters.pop_back();
                }
                letters.push_back(c);
            }
            counts[c] --;
        }
        string ans = "";
        for (char c: letters) {
            ans += c;
        }
        return ans;
    }
};