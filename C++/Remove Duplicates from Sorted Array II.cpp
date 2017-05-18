/*
Remove Duplicates from Sorted Array II
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].

思路跟I解法一致，只不过用occur记录每个元素出现的次数，可以改成3次、4次等
*/

class Solution {
public:
    int removeDuplicates(int A[], int n) {
        if(n==0) return 0;
        
        int index=0,occur=1;
        
        for(int i=1;i<n;i++){
            if(A[index]==A[i]){
                if(occur<2){
                    A[++index]=A[i];
                    occur++;
                }
            }
            else {
                A[++index]=A[i];
                occur=1;
            }
            
            
        }
        
        return index+1;

    }
};