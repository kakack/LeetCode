/*
Single Number II 

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
*/

class Solution {
public:
    int singleNumber(int A[], int n) {
        if(n==0) 
          return NULL;
        else if(n==1)
          return A[0];
          
        sort(A,A+n);
        
        int j=1;
        
        for(int i=1;i<n;i++){
            if(A[i-1]==A[i])
              j++;
            else if(j==3)
              j=1;
            else 
              return A[i-1];
        }
        
        return A[n-1];
        
        
    }
};