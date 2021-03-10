/*
Given a string s representing an expression, implement a basic calculator to evaluate it.



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
*/

#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> ops;
        ops.push(1);
        int sign = 1;

        int ret = 0;
        int n = s.length();
        int i = 0;
        while (i < n) {
            if (s[i] == ' ') {
                i ++;
            } else if (s[i] == '+') {
                sign = ops.top();
                i ++;
            } else if (s[i] == '-') {
                sign = -ops.top();
                i ++;
            } else if (s[i] == '(') {
                ops.push(sign);
                i ++;
            } else if (s[i] == ')') {
                ops.pop();
                i ++;
            } else {
                long num = 0;
                while (i < n && s[i] >= '0' && s[i] <= '9') {
                    num = num * 10 + s[i] - '0';
                    i ++;
                }
                ret += sign * num;
            }
        }
        return ret;
    }
};