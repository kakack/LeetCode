/*
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.



Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.


Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
*/

#include <string>
#include <vector>
using namespace std;

/*
    动态规划，用f[i][j]表示打印区间[i, j]的最少操作数
    case：
        1, s[1] == s[j]，那么打印左边s[i]的时候，顺便可以把右边对应的s[j]打印了，只需要考虑尽快打印完[i, j - 1]，即此时f[i][j] = f[i][j - 1]
        2, s[i] != s[j]，那么要分别完成区间左右两部分打印，记为[i, k]和[k + 1, j]，此时f[i][j] = min^(j-1)_(k=i) f[i][k] + f[k+1][j]
        3，边界条件
*/

class Solution {
public:
    int strangePrinter(string s) {
        int n = s.length();
        vector<vector<int> > f(n, vector<int>(n));
        for (int i = n - 1; i >= 0; i --) {
            f[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (s[i] == s[j]) {
                    f[i][j] = f[i][j - 1];
                } else {
                    int minn = INT_MAX;
                    for (int k = i; k < j; k ++) {
                        minn = min(minn, f[i][k] + f[k + 1][j]);
                    }
                    f[i][j] = minn;
                }
            }
        }
        return f[0][n - 1];
    }
};