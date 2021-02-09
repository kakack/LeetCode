/*
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.



Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
*/

#include <vector>

using namespace std;

class Solution {
public:
    int subarraysWithKDistinct(vector<int>& A, int K) {
        int n = A.size();
        vector<int> num1(n + 1), num2(n + 1);
        int tot1 = 0, tot2 = 0;
        int left1 = 0, left2 = 0, right = 0;
        int ret = 0;
        while (right < n) {
            if (!num1[A[right]]) {
                tot1 ++;
            }
            num1[A[right]]++;
            if (!num2[A[right]]) {
                tot2++;
            }
            num2[A[right]]++;
            while (tot1 > K) {
                num1[A[left1]]--;
                if (!num1[A[left1]]) {
                    tot1--;
                }
                left1++;
            }
            while (tot2 > K - 1) {
                num2[A[left2]] -- ;
                if (!num2[A[left2]]) {
                    tot2 --;
                }
                left2 ++;
            }
            ret += left2 - left1;
            right ++;
        }
        return ret;
    }
};