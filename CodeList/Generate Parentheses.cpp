/*
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

*/

class Solution {
public:
    vector<string> ans;
     void rec(int left,int right,string s){
            
            if(left==0&&right==0){
                this->ans.push_back(s);
                return;
            }
            if(left==0){
                rec(0,right-1,s+")");
                return;
            }
            if(right==0||left>right)
                return;
                
            rec(left-1,right,s+"(");
            rec(left,right-1,s+")");
   
        }
    vector<string> generateParenthesis(int n) {
     
        rec(n,n,"");
        return this->ans;
        
        
    }
};