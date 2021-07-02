/*
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

*/

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int idx = 0, length = arr.size();
        vector<int> res;
        if (x <= arr[0]) {
            idx = 0;
        } else if (x >= arr[length - 1]) {
            idx = length - 1;
        } else {
            for (int i = 0; i < length - 1; i ++) {
                if (arr[i] == x) {
                    idx = i;
                    break;
                } else if (arr[i] < x && arr[i + 1] > x) {
                    idx = arr[i + 1] - x >= x - arr[i] ? i : i + 1;
                }
            }
        }
        k --;
        res.push_back(arr[idx]);
        int left = idx - 1, right = idx + 1;
        while (k) {
            if (left < 0) {
                res.push_back(arr[right]);
                right ++;
            } else if (right >= length) {
                res.push_back(arr[left]);
                left --;
            } else if (x - arr[left] > arr[right] - x) {
                res.push_back(arr[right]);
                right ++;
            } else {
                res.push_back(arr[left]);
                left --;
            }
            k --;
        }
        sort(res.begin(), res.end());
        return res;

    }
};