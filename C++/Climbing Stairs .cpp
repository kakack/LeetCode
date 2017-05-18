/*
Climbing Stairs 
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

也是比较简单的，最后一步可以是2 steps或者是1 step，
那么之前需要n-2 steps或者n-1 steps，类似于斐波那契数列

递归方式超时，于是就用了循环的办法
*/

class Solution {
public:
    int climbStairs(int n) {
        int prev = 0;
        int cur = 1;
        
        for(int i=1;i<=n;i++){
            int temp=cur;
            cur+=prev;
            prev=temp;
        }
    return cur;
        
    }
};