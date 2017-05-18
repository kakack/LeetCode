/*Excel Sheet Column Number 
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
我已经不知道说什么好了……
*/

class Solution {
public:
    int titleToNumber(string s) {
        
        const int len=s.size();
        int result = 0;
        for(int i=0;i<len;i++){
            
            result=result*26+(s[i]-'A'+1);
            
        }
        
        return result;
        
    }
};