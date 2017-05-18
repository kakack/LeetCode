/*
Search in Rotated Sorted Array II 

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

跟I基本一致，但是需要注意A[mid]==A[first]的情况，这时候只要first往后走一步再看即可
*/
class Solution {
public:
    bool search(int A[], int n, int target) {
        int first=0,end=n;
        
        while(first!=end){
            int mid=(first+end)/2;
            
            if(A[mid]==target) return true;
            
            if(A[first]<A[mid]){
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
            else
               first++;
           
        }
        
        return false;
    }
};