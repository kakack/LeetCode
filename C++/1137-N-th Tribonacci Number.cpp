/*
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537


Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
*/

#include <vector>
using namespace std;
class Solution {
public:
    int tribonacci(int n) {
        vector<int> tribo(38);
        tribo[0] = 0, tribo[1] = 1,tribo[2] = 1;
        for (int i = 3; i < 38; i ++) {
            tribo[i] = tribo[i - 1] + tribo[i - 2] + tribo[i -3];
        }
        return tribo[n];
    }
};