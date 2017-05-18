/**Populating Next Right Pointers in Each Node II 
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        //我日你先人真的需要广度优先搜索啊！妈的一点偷懒都不给啊！跟某一个按层遍历树的那个题一样，先撸出那个题的结论，然后把vector里的东西处理一下
        
        vector<vector<TreeLinkNode*> > nodes;
        if(root==NULL) return;
        
        travel(root, 1, nodes);
    //这里和我自己写的循环是两种一样的处理方式    
    //     for(auto level:nodes){
    //         for(auto iter=level.begin();iter!=prev(level.end());iter++){
    //             (*iter)->next=*next(iter);
    //         }
    //  //       (*prev(level.end()))->next = NULL;
    //     }
    
       for(int i=0;i<nodes.size();i++){
           for(int j=0;j<nodes[i].size()-1;j++){
               nodes[i][j]->next=nodes[i][j+1];
           }
       }
        
        
        
    }
    
    void travel(TreeLinkNode* root, int level, vector<vector<TreeLinkNode*> > &nodes){
        if(root==NULL) return;
        
        if(level>nodes.size())
          nodes.push_back(vector<TreeLinkNode*>());
          
         nodes[level-1].push_back(root);
         travel(root->left, level+1, nodes);
         travel(root->right, level+1, nodes);
    }
};