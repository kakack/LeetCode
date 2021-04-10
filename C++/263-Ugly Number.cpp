/*
Given an integer n, return true if n is an ugly number.

Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.



Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Example 4:

Input: n = 1
Output: true
Explanation: 1 is typically treated as an ugly number.


Constraints:

-231 <= n <= 231 - 1

*/

class Solution {
public:
    bool isUgly(int n) {
        if (n == 0) {
            return false;
        }
        while (n % 2 == 0) {
            n = n / 2;
        }
        while (n % 3 == 0){
            n = n / 3;
        }
        while (n % 5 == 0){
            n = n / 5;
        }
        return n == 1;
    }
};