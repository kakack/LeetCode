
/*ZigZag Conversion 

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

这尼玛纯数学题找规律，用公式代替各个数字

*/


class Solution {
public:
    string convert(string s, int numRows) {
    string res;
    if(numRows<=1) return s;

    if (s.length()==0) {
        return res;
    }

    for (int i=0; i<numRows; i++) {
        for (int j=0,index=i; index<s.length(); j++,index =(2*numRows-2)*j+i) {
            res+=s[index];

            if ((index+(numRows-i-1)*2)<s.length()&&i!=0&&i!=numRows-1) {
                res+=s[index+(numRows-1-i)*2];
            }
        }
    }

    return res;
    }
};