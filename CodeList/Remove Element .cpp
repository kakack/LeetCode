/*
Remove Element 
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
*/

class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        
        //这个太简单了，老子都懒得sort了
        int index=0;
        for(int i=0;i<n;i++)
          if(A[i]!=elem)
            A[index++]=A[i];
            
         return index;
        
    }
};