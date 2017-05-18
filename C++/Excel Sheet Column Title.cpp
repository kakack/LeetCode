/*Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
26进制，遇到整除的时候特殊处理
*/

class Solution {
public:
    string convertToTitle(int n) {
        string res;
        while(n){
            int r=n%26;
            n=n/26;
            if(r==0){
                res.insert(res.begin(), 'Z');
                n--;
            }
            else
              res.insert(res.begin(), 'A'+r-1);
        }
        return res;
    }
};