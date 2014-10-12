/*
Median of Two Sorted Arrays 

There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


非常巧妙的每次删除某个字符串中一半的元素再来做。
每次递归的时候比较A[k/2-1]和B[k/2-1]，得到三种情况：
  1，A[k/2-1]==B[k/2-1]，那么表示已经找到了第k大的元素，直接返回即可
  2，A[k/2-1]>B[k/2-1]，表示B[0]~B[k/2-1]之间的元素全部小于AUB的第k大的元素，删除B[2k-1]以及之前所有元素，然后k变成k/2
  3，A[k/2-1]<B[k/2-1]，同理
  
  递归终止条件：
  1，A[k/2-1]==B[k/2-1]，表示找到了，返回其中任意一个
  2，k=1，返回min(A[0],B[0])
  3，A或者B是空的，返回B[k-1]或者A[k-1]
*/

class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        int num=m+n;
        if(num%2==0)
           return (find(A,m,B,n,num/2)+find(A,m,B,n,num/2+1))/2;
        else
           return find(A,m,B,n,num/2+1);
    }
    
    double find(int A[], int m, int B[], int n, int k){
        if(m>n) return find(B,n,A,m,k);//默认放成m<n，即后面一个数组比较大
        if(m==0) return B[k-1];
        if(k==1) return min(A[0],B[0]);
        
        int pa=min(k/2,m);
        int pb=k-pa;
        
        if(A[pa-1]>B[pb-1])
           return find(A,m,B+pb,n-pb,k-pb);
        else if(A[pa-1]<B[pb-1])
           return find(A+pa,m-pa,B,n,k-pa);
        else
           return A[pa-1];
        
        
    }
};