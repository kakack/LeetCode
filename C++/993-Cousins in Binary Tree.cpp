/*
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

using namespace std;
class Solution {
private:
    int x, y;
    TreeNode* parent_x;
    TreeNode* parent_y;
    int depth_x, depth_y;
    bool found_x, found_y;

public:
    void dfs(TreeNode* node, int depth, TreeNode* parent) {
        if (!node) {
            return;
        }
        if (node->val == x) {
            tie(parent_x, depth_x, found_x) = tuple{parent, depth, true};
        } else if (node->val == y) {
            tie(parent_y, depth_y, found_y) = tuple{parent, depth, true};
        }

        if (this->found_x && this->found_y) {
            return;
        }
        dfs(node->left, depth + 1, node);
        if (this->found_x && this->found_y) {
            return;
        }
        dfs(node->right, depth + 1, node);
    } 
    bool isCousins_(TreeNode* root, int x, int y) {
        this->x = x;
        this->y = y;
        dfs(root, 0, nullptr);
        return depth_x == depth_y && parent_x != parent_y;
    }

    void update(TreeNode* node, TreeNode* parent, int depth) {
        if (node->val == x) {
            tie(parent_x, depth_x, found_x) = tuple{parent, depth, true};
        } else if (node->val == y) {
            tie(parent_y, depth_y, found_y) = tuple{parent, depth, true};
        }
    }

    bool isCousins(TreeNode* root, int x, int y) {
        this->x = x;
        this->y = y;
        queue<pair<TreeNode*, int>> q;
        q.emplace(root, 0);
        update(root, nullptr, 0);
        while (!q.empty()) {
            auto&& [node, depth] = q.front();
            if (node->left) {
                q.emplace(node->left, depth + 1);
                update(node->left, node, depth + 1);
            }
            if (node->right) {
                q.emplace(node->right, depth + 1);
                update(node->right, node, depth + 1);
            }
            if (found_x && found_y) {
                break;
            }
            q.pop();
        }
        return depth_x == depth_y && parent_x != parent_y;
    }
};