/*Integer to Roman
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
*/

class Solution {
public:
    string intToRoman(int num) {
        const int radix[] = {1000,900,500,400,100,90,50,40,10,9,5,4,1};//我实在是不太了解罗马字符，只能依样画葫芦了
        
        const string symbol[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        
        string roman;
        
        for(int i = 0;num >0;i++){
            int count = num / radix[i];
            num%=radix[i];
            for(;count>0;count--) roman+=symbol[i];//和一般的十进制不同的是，进位的更多了
            
        }
        return roman;
    }
};