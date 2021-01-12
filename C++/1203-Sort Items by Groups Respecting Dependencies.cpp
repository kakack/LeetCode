/*
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.



Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.


Constraints:

1 <= m <= n <= 3 * 104
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
*/

class Solution {
public:
    vector<int> topSort(vector<int>& deg, vector<vector<int>>& graph, vector<int>& items) {
        queue<int> Q;
        for (auto& item: items) {
            if (deg[item] == 0) {
                Q.push(item);
            }
        }
        vector<int> res;
        while (!Q.empty()) {
            int u = Q.front();
            Q.pop();
            res.emplace_back(u);
            for (auto& v: graph[u]) {
                if (--deg[v] == 0) {
                    Q.push(v);
                }
            }
        }
        return res.size() == items.size() ? res : vector<int>{};
    }

    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
        vector<vector<int>> groupItem(n + m);

        // 组间和组内依赖图
        vector<vector<int>> groupGraph(n + m);
        vector<vector<int>> itemGraph(n);

        // 组间和组内入度数组
        vector<int> groupDegree(n + m, 0);
        vector<int> itemDegree(n, 0);

        vector<int> id;
        for (int i = 0; i < n + m; ++i) {
            id.emplace_back(i);
        }

        int leftId = m;
        // 给未分配的 item 分配一个 groupId
        for (int i = 0; i < n; ++i) {
            if (group[i] == -1) {
                group[i] = leftId;
                leftId += 1;
            }
            groupItem[group[i]].emplace_back(i);
        }
        // 依赖关系建图
        for (int i = 0; i < n; ++i) {
            int curGroupId = group[i];
            for (auto& item: beforeItems[i]) {
                int beforeGroupId = group[item];
                if (beforeGroupId == curGroupId) {
                    itemDegree[i] += 1;
                    itemGraph[item].emplace_back(i);
                } else {
                    groupDegree[curGroupId] += 1;
                    groupGraph[beforeGroupId].emplace_back(curGroupId);
                }
            }
        }

        // 组间拓扑关系排序
        vector<int> groupTopSort = topSort(groupDegree, groupGraph, id);
        if (groupTopSort.size() == 0) {
            return vector<int>{};
        }
        vector<int> ans;
        // 组内拓扑关系排序
        for (auto& curGroupId: groupTopSort) {
            int size = groupItem[curGroupId].size();
            if (size == 0) {
                continue;
            }
            vector<int> res = topSort(itemDegree, itemGraph, groupItem[curGroupId]);
            if (res.size() == 0) {
                return vector<int>{};
            }
            for (auto& item: res) {
                ans.emplace_back(item);
            }
        }
        return ans;
    }
};
