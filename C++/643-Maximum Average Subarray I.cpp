/*
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
*/

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int sums = accumulate(nums.begin(), nums.begin() + k, 0);
        double res = (double)sums / k;
        for (int i = 1; i <= nums.size() - k; i ++) {
            sums = sums - nums[i - 1] + nums[i + k - 1];
            res = max(res, (double)sums/ k);
        }
        return res;
    }
};