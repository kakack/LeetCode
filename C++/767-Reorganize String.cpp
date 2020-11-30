/*
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

当 nn 是偶数时，有 n/2n/2 个偶数下标和 n/2n/2 个奇数下标，因此每个字母的出现次数都不能超过 n/2n/2 次，否则出现次数最多的字母一定会出现相邻。

当 nn 是奇数时，由于共有 (n+1)/2(n+1)/2 个偶数下标，因此每个字母的出现次数都不能超过 (n+1)/2(n+1)/2 次，否则出现次数最多的字母一定会出现相邻。

由于当 nn 是偶数时，在整数除法下满足 n/2n/2 和 (n+1)/2(n+1)/2 相等，因此可以合并 nn 是偶数与 nn 是奇数的情况：如果可以重新排布成相邻的字母都不相同的字符串，每个字母最多出现 (n+1)/2(n+1)/2 次。

因此首先遍历字符串并统计每个字母的出现次数，如果存在一个字母的出现次数大于 (n+1)/2(n+1)/2，则无法重新排布字母使得相邻的字母都不相同，返回空字符串。如果所有字母的出现次数都不超过 (n+1)/2(n+1)/2，则考虑如何重新排布字母。

*/
#include "string"
#include "vector"
#include "queue"
using namespace std;

class Solution {
public:
    string reorganizeString(string S) {
        if (S.length() < 2){
            return S;
        }
        vector<int > counts(26, 0);
        int maxCount = 0;
        int length = S.length();
        for (int i=0; i < length; i++) {
            char c = S[i];
            counts[c - 'a'] ++;
            maxCount = max(maxCount, counts[c - 'a']);
        }
        if  (maxCount > (length + 1) / 2) {
            return "";
        }
        auto cmp = [&](const char& letter1, const char& letter2) {
            return counts[letter1 - 'a'] < counts[letter2 - 'a'];
        };
        priority_queue<char, vector<char>, decltype(cmp)> queue{cmp};
        for (char c = 'a'; c <= 'z'; c++) {
            if (counts[c - 'a'] > 0) {
                queue.push(c);
            }
        }
        string sb = "";
        while (queue.size() > 1) {
            char letter1 = queue.top();
            queue.pop();
            char letter2 = queue.top();
            queue.pop();
            sb += letter1;
            sb += letter2;
            int index1 = letter1 - 'a', index2 = letter2 - 'a';
            counts[index1] --;
            counts[index2] --;
            if (counts[index1] > 0) {
                queue.push(letter1);
            }
            if (counts[index2] > 0) {
                queue.push(letter2);
            }
        }
        if (queue.size() > 0) {
            sb += queue.top();
        }
        return sb;
    }
};