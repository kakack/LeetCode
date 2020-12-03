/*
Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

同 316
*/

#include "vector"
#include "map"
#include "string"
#include "algorithm"

using namespace std;


class Solution {
public:
    string smallestSubsequence(string s) {
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