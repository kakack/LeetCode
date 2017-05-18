/*
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
*/

class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        
        if(s.length()==0||s[0]==')'||s[0]==']'||s[0]=='}')
          return false;
        else  
          stack.push_back(s[0]);
        
        for(int i=1;i<s.length();i++){
            if(s[i]=='('||s[i]=='['||s[i]=='{'){
              stack.push_back(s[i]);
              continue;
            }
            
            char cur=stack.back();
            
            if(s[i]==')'&&cur!='(')
               return false;
            if(s[i]==']'&&cur!='[')
               return false;
            if(s[i]=='}'&&cur!='{')
               return false;
            
            stack.pop_back();
        }
        
        if(stack.size()!=0)
          return false;
        else
          return true;
        
        
    }
};