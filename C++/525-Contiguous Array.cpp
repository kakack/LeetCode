/*
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

由于「00 和 11 的数量相同」等价于「11 的数量减去 00 的数量等于 00」，我们可以将数组中的 00 视作 -1−1，则原问题转换成「求最长的连续子数组，其元素和为 00」。

实现方面，不需要创建数组 newNums 和 prefixSums，只需要维护一个变量 counter 存储 newNums 的前缀和即可

具体做法是，遍历数组 nums，当遇到元素 11 时将 counter 的值加 1，当遇到元素 0 时将 counter 的值减 1，遍历过程中使用哈希表存储每个前缀和第一次出现的下标。

规定空的前缀的结束下标为 −1，由于空的前缀的元素和为 0，因此在遍历之前，首先在哈希表中存入键值对 (0,−1)。遍历过程中，对于每个下标 i，进行如下操作：

    如果 counter 的值在哈希表中已经存在，则取出 counter 在哈希表中对应的下标 prevIndex，nums 从下标 prevIndex+1 到下标 i 的子数组中有相同数量的 0 和 1，该子数组的长度为 i−prevIndex，使用该子数组的长度更新最长连续子数组的长度；

    如果 counter 的值在哈希表中不存在，则将当前余数和当前下标 i 的键值对存入哈希表中。

*/

#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int MaxLength = 0;
        unordered_map<int, int> mp;
        int counter = 0;
        mp[counter] = -1;
        int n = nums.size();
        for (int i = 0; i < n; i ++) {
            int num = nums[i];
            if (num == 1) {
                counter ++;
            } else {
                counter --;
            }
            if (mp.count(counter)) {
                int prevIndex = mp[counter];
                MaxLength = max(MaxLength, i - prevIndex);
            } else {
                mp[counter] = i;
            }
        }
        return MaxLength;
    }
};