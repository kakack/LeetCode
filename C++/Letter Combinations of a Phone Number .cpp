/*Letter Combinations of a Phone Number 

My Submissions Question Solution 
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
*/

class Solution {
public:

    const vector<string> keyword {"","","abc","def","ghi","jkl","mno", "pqrs","tuv","wxyz"};
    
    void dfs(string &digits, size_t cur, string path, vector<string> &result){
        
        if(cur == digits.size()){
            result.push_back(path);
            return ;
        }
        
        for(char c: keyword[digits[cur] - '0'])
           dfs(digits, cur+1, path+c, result);
    }
    
    vector<string> letterCombinations(string digits) {
        
        vector<string> result;
        
        if(digits.size() == 0)
          return result;
        
        dfs(digits, 0, "", result);
        
        return result;
        
    }
    

};