/*
Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
我一开始是想用最蠢的办法，从左往右扫一边然后找到每个能容雨的池子然后叠加，后来编码时候发现这办法真是蠢爆肝了，蠢的我天怒人怨各种要回溯修改。

然后发现一个好办法，先找到最高的一个柱子，然后在对其左右分别处理
这样至少节约了很多回溯过程，简单两边的操作都是对称的，极易处理
*/

class Solution {
public:
    int trap(int A[], int n) {
        
        int max = 0; // 最高的柱子,将数组分为两半 
          for (int i = 0; i < n; i++)
              if (A[i] > A[max]) 
                max = i;
          
          int water = 0;
          for (int i = 0, peak = 0; i < max; i++)
              if (A[i] > peak) 
                 peak = A[i];
              else
                  water += peak - A[i];
          for (int i = n - 1, top = 0; i > max; i--)
              if (A[i] > top) 
                 top = A[i];
              else 
                 water += top - A[i];
          return water;
        
    }
};