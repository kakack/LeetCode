/*
First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

*/

class Solution {
public:
    int firstMissingPositive(int A[], int n) {
        int i =0, max=0,j=0;
     int flag=0;
     int missingPositive=0;
     for(i=0;i<n;i++)
     {
         if(A[i]>max)
             max = A[i];
     }
     if(max==1)
         return 2;
     for(i=1;i<max;i++)
     {
         for(j=0;j<n;j++)
             {
                 flag=0;
                if(A[j]==i)
                    {
                    flag=1;
                    break;
                    }
             }
         if(flag!=1)
             return i;

     }

     return max+1;
        
    }
};