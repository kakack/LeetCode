/*
896. Monotonic Array
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000*/


#include <vector>

using namespace std;

class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        int n = A.size(), start = 1;
        if(n <= 2) {
            return true;
        }
        bool increase = true;
        while (start < n)
        {
            if (A[start - 1] == A[start]) {
                start ++;
                continue;
            } else if (A[start] > A[start - 1])
            {
                break;
            } else {
                increase = false;
                break;
            }
        }
        for (int i = start; i < n; i ++){
            if (A[i] == A[i - 1]) {
                continue;
            } elif (increase != (A[i] > A[i - 1])) {
                return false;
            }
        }
        return true;
    }
};