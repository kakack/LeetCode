/*Pow(x, n)分治法
Implement pow(x, n).
*/

class Solution {
public:
    double pow(double x, int n) {
        if(n == 0)
          return 1;
        double res = pow(x, n/2);
        if(n%2 == 0)
          return res*res;
        else
          return res*res*x;
        
    }
    double myPow(double x, int n) {
        if(n<0)
          return 1.0/pow(x, -n);
        else
          return pow(x,n);
    }
};