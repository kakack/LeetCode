/*
Single Number 

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

解法：利用相同两个数字异或得0的特征来做最简单，可以思考如果一组数组中大家都出现三次某个出现一次或者两次的怎么做
*/



class Solution {
public:
    int singleNumber(int A[], int n) {
        int ans=A[0];
        for(int i=1;i<n;i++)
           ans=ans^A[i];
        return ans;   
    }
};