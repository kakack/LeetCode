
/*
3Sum Closest 
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

这题跟3Sum类似，其实不算多难的题目，只不过是涉及到vector一些巧妙的计算，关于容器和迭代器的内容确实需要好好看一下

然后这里的主要思路就是先排序，然后夹逼定理来做
*/
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        int ans,min=INT_MAX;
        if(num.size()<3) return ans;
        sort(num.begin(),num.end());
        
        
          for (auto a = num.begin(); a != prev(num.end(), 2);a = upper_bound(a, prev(num.end(), 2), *a)){
              auto b = next(a);
              auto c = prev(num.end());
              
              while(b<c){
                  int sum=*a+*b+*c;
                  int distance=abs(target-sum);
                  
                  if(distance<min){
                      ans=sum;
                      min=distance;
                  }
                  
                  if(sum<target)
                     b++;
                  else
                     c--;
              }
          }
        return ans;
    }
};