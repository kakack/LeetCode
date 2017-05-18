/*Search a 2D Matrix 
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
这个也没啥好说的
*/

class Solution {
public:
    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        
        int row = 0, n = matrix.size();//总共有n行
        
        if(target<matrix[0][0])
          return false;
        
        for(;row<n;row++){
            if(matrix[row][0]>target)
              break;
        }
        
        row--;
        
        int column = 0, m = matrix[row].size();//那一行有m列
        
        for(;column<m;column++){
            if(matrix[row][column] == target)
               return true;
        }
        
        
        return false;
        
        
        
        
    }
};