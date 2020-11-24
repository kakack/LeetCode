/*
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6*/

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


 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };


class Solution1 {
public:
    int countNodes(TreeNode* root) {
        int count = 0;
        dfs(root, count);
        return count;
    }

    void dfs(TreeNode* root, int &count) {
        if (root != nullptr) {
            dfs(root->left, count);
            count ++;
            dfs(root->right, count);
        }
    }
};

class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        int height = 0;
        TreeNode* cur = root;
        while (cur->left != nullptr) {
            height ++;
            cur = cur->left;
        }
        int low  = 1 << height, high = (1 << (height + 1)) - 1;
        while (low < high) {
            int mid = (high - low + 1) / 2 + low;
            if (exist(root, height, mid)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    bool exist(TreeNode* root, int height, int k) {
        int bits = 1 << (height - 1);
        TreeNode* cur = root;
        while (root != nullptr && bits > 0) {
            if (!(bits & k)) {
                cur = cur->left;
            } else {
                cur = cur->right;
            }
            bits >>= 1;
        }
        return cur != nullptr;
    }
};