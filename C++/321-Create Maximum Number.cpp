/*
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]

单调栈
对于每一组 xx 和 yy 的值，
得到最大数的过程分成两步，
第一步是分别从两个数组中得到指定长度的最大子序列，
第二步是将两个最大子序列合并。
*/

#include "vector"
using namespace std;

class Solution {
public:
    vector<int> pickMax(vector<int>& nums, int k) {
        vector<int> stack;
        int drop = nums.size() - k;
        for (int num:nums) {
            while (drop > 0 && !stack.empty() && stack.back() < num) {
                stack.pop_back();
                drop --;
            }
            stack.push_back(num);
        }
        vector<int> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back(stack[i]);
        }
        return ans;
    }

    int compare(vector<int>& numsA, int index1, vector<int>& numsB, int index2) {
        int x = numsA.size(), y = numsB.size();
        while (index1 < x && index2 < y) {
            int difference = numsA[index1] - numsB[index2];
            if (difference != 0) {
                return difference;
            }
            index1++;
            index2++;
        }
        return (x - index1) - (y - index2);
    }


    vector<int> merge(vector<int>& numsA, vector<int>& numsB) {
        int x = numsA.size(), y = numsB.size();
        if (x == 0) {
            return numsB;
        }
        if (y == 0) {
            return numsA;
        }
        int mergeLength = x + y;
        vector<int> merged(mergeLength);
        int index1 = 0, index2 = 0;
        for (int i = 0; i < mergeLength; i++) {
            if (compare(numsA, index1, numsB, index2) > 0) {
                merged[i] = numsA[index1++];
            } else {
                merged[i] = numsB[index2++];
            }
        }
        return merged;
    }
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        int m = nums1.size(), n = nums2.size();
        vector<int> maxSubsequence(k, 0);
        int start = max(0, k - n), end = min(k, m);
        for (int i = start; i <= end; i++) {
            vector<int> subsequence1(pickMax(nums1, i));
            vector<int> subsequence2(pickMax(nums2, k - i));
            vector<int> curMaxSubsequence(merge(subsequence1, subsequence2));
            if (compare(curMaxSubsequence, 0, maxSubsequence, 0) > 0) {
                maxSubsequence.swap(curMaxSubsequence);
            }
        }
        return maxSubsequence;
    }
};