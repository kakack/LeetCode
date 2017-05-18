/*Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

(1) 在height尾部添加一个0，也就是一个高度为0的立柱。作用是在最后也能凑成上面提的那种“波峰图”。

(2) 定义了一个stack，然后遍历时如果height[i] 大于stack.top()，进栈。反之，出栈直到栈顶元素小于height[i]。
*/

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int largestRectangleArea(vector<int> &height) {
	
	stack<int> s;
	int sum = 0;
	height.push_back(0);
	
	for (int i = 0;i < height.size();i++) {
		cout<<"i="<<i<<endl;
				
		
		if(s.empty()||height[i] > height[s.top()]){
		   
		   s.push(i);
		
		//   cout<<"插进去了"<<height[i]<<endl;
		}
		
		else{
			int tmp = s.top();
			s.pop();
		//	cout<<"拿出来了"<<height[tmp]<<endl;
			sum = max(sum, height[tmp]*(s.empty()? i : i-s.top()-1));  
		//	cout<<"算了一下是"<<height[tmp]*(s.empty()? i : i-s.top()-1)<<endl;
			i--;  
		}
		
		
	}
	return sum;
	
        
}
int main(int argc, char *argv[]) {
  int vi[8]={7,5,5,6,8,7,2,10};
  vector<int> h;
  for (int i=0;i<8;i++) {
	 h.push_back(vi[i]);
	
}
  cout<<largestRectangleArea(h);
}