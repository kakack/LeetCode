/*
Search in Rotated Sorted Array
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
*/

class Solution {
public:
    int search(int A[], int n, int target) {
        int first=0,end=n;
        
        if(n==1&&A[0]==target) return 0;
        
        
        
        while(first!=end){
            int mid=(first+end)/2;
            
            if(A[mid]==target) return mid;
            
            if(A[first]<=A[mid]){
                if(A[mid]>target&&A[first]<=target){
                    end=mid;
                }
                else
                   first=mid+1;
            }
            else if(A[mid]<A[first]){
                if(A[mid]<target&&A[end-1]>=target){
                    first=mid+1;
                }
                else
                   end=mid;
            }
           
        }
        
        return -1;
          
        
        
    }
};