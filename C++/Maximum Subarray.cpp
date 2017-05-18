/*
Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

解法：这里先写了O(n)的解法。分治的我已经有思路了，可以很快写一个

    因为最大连续子序列和只可能是以位置0～n-1中某个位置结尾。
    当遍历到第i个元素时，判断在它前面的连续子序列和是否大于0，
    如果大于0，则以位置i结尾的最大连续子序列和为元素i和前门的连续子序列和相加；
    否则，则以位置i结尾的最大连续子序列和为元素i。
    
    

*/

class Solution {
    

public:
    int maxSubArray(int A[], int n) {
        int maxsum=A[0],maxhere=A[0];
        
        for(int i=1;i<n;i++){
            if(maxhere<=0)
               maxhere=A[i];
            else
               maxhere+=A[i];
               
            if(maxhere>maxsum)
              maxsum=maxhere;
            
        }
        
        return maxsum;
        
    }
};