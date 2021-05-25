/*
You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.



Example 1:

Input: nums = [1,2,0,3,0], k = 1
Output: 3
Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
Example 2:

Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
Output: 3
Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
Example 3:

Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
Output: 3
Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].


Constraints:

1 <= k <= nums.length <= 2000
​​​​​​0 <= nums[i] < 210
*/

class Solution {
private:
    // x 的范围为 [0, 2^10)
    static constexpr int MAXX = 1 << 10;
    // 极大值，为了防止整数溢出选择 INT_MAX / 2
    static constexpr int INFTY = INT_MAX / 2;

public:
    int minChanges(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> f(MAXX, INFTY);
        // 边界条件 f(-1,0)=0
        f[0] = 0;

        for (int i = 0; i < k; ++i) {
            // 第 i 个组的哈希映射
            unordered_map<int, int> cnt;
            int size = 0;
            for (int j = i; j < n; j += k) {
                ++cnt[nums[j]];
                ++size;
            }

            // 求出 t2
            int t2min = *min_element(f.begin(), f.end());

            vector<int> g(MAXX, t2min);
            for (int mask = 0; mask < MAXX; ++mask) {
                // t1 则需要枚举 x 才能求出
                for (auto [x, countx]: cnt) {
                    g[mask] = min(g[mask], f[mask ^ x] - countx);
                }
            }

            // 别忘了加上 size
            for_each(g.begin(), g.end(), [&](int& val) {val += size;});
            f = move(g);
        }

        return f[0];
    }
};
