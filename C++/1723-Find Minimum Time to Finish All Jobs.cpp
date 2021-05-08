/*You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.



Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.
Example 2:

Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.


Constraints:

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107
*/

#include <vector>

using namespace std;

class Solution {
public:
    bool backtrack(vector<int>& jobs, vector<int>& workloads, int idx, int limit) {
        if (idx >= jobs.size()) {
            return true;
        }
        int cur = jobs[idx];
        for (auto& workload: workloads) {
            if (workload + cur <= limit) {
                workload += cur;
                if (backtrack(jobs, workloads, idx + 1, limit)) {
                    return true;
                }
                workload -= cur;
            }
            if (workload == 0 || workload + cur == limit) {
                break;
            }
        }
        return false;
    }

    bool check(vector<int>& jobs, int k, int limit) {
        vector<int> workloads(k, 0);
        return backtrack(jobs, workloads, 0, limit);
    }

    int minimumTimeRequired(vector<int>& jobs, int k) {
        sort(jobs.begin(), jobs.end(), greater<int>());
        int l = jobs[0], r = accumulate(jobs.begin(), jobs.end(), 0);
        while (l < r) {
            int mid = (l + r) >> 1;
            if (check(jobs, k, mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};