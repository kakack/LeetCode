/*
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.



Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
*/

#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int longestSubstring(string s, int k) {
        int ret = 0;
        int n = s.length();
        for (int i = 1; i <= 26; i ++) {
            int l = 0, r = 0;
            vector<int> cnt(26, 0);
            int tot = 0, less = 0;
            while (r < n) {
                cnt[s[r] - 'a'] ++;
                if (cnt[s[r] - 'a'] == 1) {
                    tot ++;
                    less ++;
                }
                if (cnt[s[r] - 'a'] == k) {
                    less--;
                }
                while (tot > i) {
                    cnt[s[l] - 'a'] --;
                    if (cnt[s[l] - 'a'] == k - 1) {
                        less++;
                    }
                    if (cnt[s[l] - 'a'] == 0) {
                        tot --;
                        less --;
                    }
                    l ++;
                }
                if (less == 0) {
                    ret = max(ret, r - l + 1);
                }
                r ++;
            }
        }
        return ret;
    }
};