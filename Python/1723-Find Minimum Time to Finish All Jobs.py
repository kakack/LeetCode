# -*- coding: utf-8 -*
"""
@author: Kai Chen
@file: 1723-Find Minimum Time to Finish All Jobs.py
@time: 2021/5/8 10:38
@desc:
You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

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
"""


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        def check(limit):
            # 剪枝：排序后，大的先拿出来试，如果方案不行，失败得更快
            arr = sorted(jobs)

            groups = [0] * k
            # 分成K 组，看看在这个limit 下 能不能安排完工作
            if backtrace(arr, groups, limit):
                return True
            else:
                return False

        def backtrace(arr, groups, limit):
            # 尝试每种可能性
            # print(arr, groups, limit)
            if not arr: return True  # 分完，则方案可行
            v = arr.pop()

            for i in range(len(groups)):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr, groups, limit):
                        return True
                    groups[i] -= v

                    # 剪枝，如果这个工人没分到活，那别人肯定得多干活了，那最后的结果必然不是最小的最大值，就不用继续试了。
                    if groups[i] == 0:
                        break

            arr.append(v)

            return False

        # 每个人承担的工作的上限，最小为，job 里面的最大值，最大为 jobs 之和
        l, r = max(jobs), sum(jobs)

        while l < r:
            mid = (l + r) // 2

            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l
