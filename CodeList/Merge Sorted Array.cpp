/*Merge Sorted Array 

Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
*/

class Solution {
public:
//从后面往前面merge比从前往后merge要好，因为从前往后会把之前A[]override掉
    void merge(int A[], int m, int B[], int n) {
        int nA = m-1, nB = n-1, nT = m+n-1;
        
        while(nA>=0&&nB>=0){
            A[nT--] = A[nA] >= B[nB]? A[nA--]:B[nB--];
        }
        
        while(nB>=0)
            A[nT--] = B[nB--];
    }
    
};