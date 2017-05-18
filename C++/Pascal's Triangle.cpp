/*
Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/

class Solution {
public:
// long factorial(long n){
// 	 if(n==0)
// 	    return 1;
// 	 else
// 	    return factorial(n-1)*n; 
// 	   }

// int C(long n,long r){
// 	 return int(factorial(n)/(factorial(r)*factorial(n-r)));
// }

int C(int n,int r){
   int ans=1;
	if(r==0)
	   return ans;	
	else
	   for(int i=1;i<=r;i++){
	     ans=ans*(n-r+i)/i;
	}
	return ans;
  }
   
    vector<vector<int> > generate(int numRows) {
        vector<vector<int> > ans;
        for(int i=0;i<long(numRows);i++){
            vector<int> row;
            for(long j=0;j<=i;j++){
                row.push_back(C(i,j));
            }
            
            ans.push_back(row);
        }
        
        return ans;     
    }
};