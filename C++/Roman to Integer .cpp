/*
Roman to Integer 
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
*/
//从前往后扫描，用一个临时变量记录分段数字。 如果当前比前一个大，说明这一段的值应该是当前这个值减去上一个值。比如 IV = 5 – 1；否 则，将当前值加入到结果中，然后开始下一段记录。比如 VI = 5 + 1, II=1+1
class Solution {
public:

    inline int map(const char c){
        switch(c){
            
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
    
    int romanToInt(string s) {
        int result = 0;
        for(int i = 0; i<s.size();i++){
            if(map(s[i])>map(s[i-1]))
              result += (map(s[i])-2*map(s[i-1]));//减去2倍是因为之前多加了一遍
            else
              result +=map(s[i]);
        }
        
        return result;
    }
};