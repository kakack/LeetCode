/*
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?



Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [0]
Output: 0
Example 3:

Input: nums = [2,4]
Output: 6
Example 4:

Input: nums = [8,10,2]
Output: 10
Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127


Constraints:

1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1

*/

#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int x = 0, high_bit = 30;
        for (int k = high_bit; k >=0; k--) {
            unordered_set<int> seen;
            for (auto num: nums) {
                seen.insert(num >> k);
            }
            int x_next = x * 2 + 1;
            bool found = false;
            for (auto num: nums) {
                if (seen.count(x_next ^ (num >> k))) {
                    found = true;
                    break;
                }
            }
            if (found) {
                x = x_next;
            } else {
                x = x_next - 1;
            }
        }
        return x;
    }
};