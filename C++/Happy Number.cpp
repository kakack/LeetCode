/*Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

用set模拟，中间值都存到set里，如果循环了就false如果出1了就true

*/

class Solution {
public:
    int cal(int num){
        int res = 0;
        while(num){
            res+=(num%10)*(num%10);
            num = num/10;
        }
        return res;
    }

    bool isHappy(int n) {
       set<int> tmp;
    
        while(n!=1){
            if(tmp.find(n)==tmp.end())
                tmp.insert(n);
            else
                return false;
            n=cal(n);
        }
        return true;
    }
};